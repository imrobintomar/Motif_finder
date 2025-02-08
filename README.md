
Sequence Pattern Extraction Tool

This tool is designed to extract protein sequence patterns using the ScanProsite tool from ExPASy and save the results in a CSV file. The tool reads a FASTA file, extracts protein sequences, scans for Prosite signatures, and retrieves the corresponding consensus patterns from the Prosite database.

Requirements

To run this tool, ensure you have the following dependencies installed:

Biopython: A set of Python tools for computational biology.

requests: For making HTTP requests to retrieve pattern data from the Prosite database.


You can install the required dependencies with the following:

pip install biopython requests

Files

1. Sequence1.fasta: This is the input file containing protein sequences in FASTA format. Each sequence should be preceded by a header starting with a '>' symbol, followed by the protein identifier and sequence.


2. sequence_pattern_new.csv: The output CSV file that will contain the protein identifiers, sequences, and the extracted Prosite pattern information.


3. log.txt: This log file records the success or failure of each sequence processing, providing useful debug information.



How it Works

1. readInputFile

Reads the protein sequences from Sequence1.fasta and processes each sequence.

Extracts the protein identifier and sequence and sends it to the outputCSVFile function for processing.


2. writeLogFile

Logs the status of each sequence, including whether it was processed successfully or encountered an error.

This log file is used for tracking progress and debugging errors.


3. outputCSVFile

For each sequence, the tool:

1. Extracts the protein identifier.


2. Strips newline characters from the sequence.


3. Uses the ScanProsite tool to scan the sequence for Prosite signatures.


4. Retrieves the consensus patterns for each signature from the Prosite website.


5. Saves the protein identifier, sequence, and the patterns into the sequence_pattern_new.csv file.




4. Error Handling

Errors during sequence processing are logged to the log.txt file with the status "UnSuccessful".

Successful sequence processing is logged with the status "Successful".


5. Request Rate Limiting

To avoid overloading the Prosite server, the tool waits 2 seconds between requests (time.sleep(2)).


Usage

1. Place your protein sequences in a FASTA file named Sequence1.fasta.


2. Run the Python script:

python script_name.py


3. The results will be saved in a CSV file (sequence_pattern_new.csv) with columns for protein ID, sequence, and the corresponding Prosite pattern. Logs will be written to log.txt.



Example of CSV Output

The resulting sequence_pattern_new.csv will look like this:

Logs

log.txt will contain entries such as:

P12345    Successful

P67890    ServerError

P98765    UnSuccessful



Troubleshooting

ServerError: Occurs when there's an issue retrieving the consensus pattern from the Prosite website. This could be due to server issues or an invalid signature.

UnSuccessful: The sequence could not be processed due to an error in the code or invalid input.


