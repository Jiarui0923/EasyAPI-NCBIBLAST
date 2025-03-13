import requests
import time
import io
import xml.etree.ElementTree as ET

def submit_blast(sequence, email, program='blastp', database='uniref50', expect=10, word_size=3, matrix='BLOSUM62', histlist_size=100):
    url = 'https://www.ebi.ac.uk/Tools/services/rest/ncbiblast/run'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'program': program,
        'database': database,
        'sequence': sequence,
        'except': int(expect),
        'word_size': int(word_size),
        'matrix': matrix,
        'stype': 'protein',
        'histlist_size': histlist_size,
        'email': email
    }
    
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200: return response.text
    else: raise ConnectionError("Failed to submit job.")

def check_status(job_id):
    url = f'https://www.ebi.ac.uk/Tools/services/rest/ncbiblast/status/{job_id}'
    response = requests.get(url)
    if response.status_code == 200: return response.text
    else: raise ConnectionError("Failed to get job status.")

def retrieve_results(job_id):
    url = f'https://www.ebi.ac.uk/Tools/services/rest/ncbiblast/result/{job_id}/xml'
    response = requests.get(url)
    if response.status_code == 200: return response.text
    else: raise ConnectionError("Failed to get job results.")

def write_unaligned_fasta_from_xml(blast_xml):
    tree = ET.parse(blast_xml)
    root = tree.getroot()
    ns = {'': 'http://www.ebi.ac.uk/schema'}
    hits = root.findall('.//hit', ns)
    output = ""
    for hit in hits:
        hit_id = hit.get('id')
        hit_seq = hit.find('.//matchSeq', ns).text
        output += f">{hit_id}\n"
        output += f"{hit_seq}\n"
    return output
        
def get_unaligned_seqs(seq, program='blastp', database='uniref50', expect=10, word_size=3, matrix='BLOSUM62', histlist_size=100):
    email = 'your.email@example.com'
    job_id = submit_blast(seq, email, program=program, database=database, expect=expect, word_size=word_size, matrix=matrix, histlist_size=histlist_size)
    if job_id:
        status = check_status(job_id)
        while status == 'RUNNING' or status == 'WAITING':
            time.sleep(30)
            status = check_status(job_id)
    if status == 'FINISHED': 
        blast_xml = retrieve_results(job_id)
        if blast_xml:
            blast_xml = io.StringIO(blast_xml)
            data = write_unaligned_fasta_from_xml(blast_xml)
            return data
    else:
        raise Exception("Job failed or did not complete.")


def blast_fasta(sequence, algorithm='blastp', db='uniref50',
                num_worker=16, expect_value=10, word_size=3,
                max_target_seqs=500, matrix='BLOSUM62'):
    _blast_out = get_unaligned_seqs(seq=sequence, program=algorithm, database=db,
                                    expect=expect_value, word_size=word_size, matrix=matrix,
                                    histlist_size=max_target_seqs)
    return _blast_out