setup:
	pip install biopython

search-for-gene: 
	@python print.py "Prepare N_BASE_CODE and N_BASE_GENE..." White; 
	
	@N_BASE_CODE=$$(mktemp);
	@N_BASE_GENE=$$(mktemp);

	@python read-fna-file.py $(filter-out search-for-gene, $(MAKECMDGOALS)) > N_BASE_CODE;
	@python read-fna-file.py input 0 > N_BASE_GENE;
	
	@python print.py "Preporation done, starting to search for gene." Green;
	
	@python print.py "Search for gene 5' to 3'" White;
	@python search-for-gene.py;

	@python print.py "Search for gene 3' to 5'" White;
	@python flip-genome.py N_BASE_GENE;
	@python search-for-gene.py;

test:
	@N_BASE_CODE=$$(mktemp);
	@python read-fna-file.py $(filter-out test, $(MAKECMDGOALS)) > N_BASE_CODE;
	@python test.py;
	
%::
	@true