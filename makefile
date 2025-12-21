setup:
	pip install biopython

search-for-gene: 
	N_BASE_CODE=$$(mktemp);

	N_BASE_GENE=$$(mktemp);

	python read-fna-file.py $(filter-out search-for-gene, $(MAKECMDGOALS)) > N_BASE_CODE;
	python read-fna-file.py input 0 > N_BASE_GENE;
	
	python search-for-gene.py;
	
%::
	@true