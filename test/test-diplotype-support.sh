check()
{
	if diff $1 $2; then
    	echo ok
	else
    	echo fail
	fi
}
###########################################################################
#1. Test loading no called genotypes 
###########################################################################
gemini load -v non-variants-included-snippet.vcf.gz --skip-gene-tables --skip-gerp-bp --skip-cadd non-variants-included-snippet.db

echo "    load.t1...\c"
echo "chr1	96078437	96078438	A	
chr1	96078438	96078439	T	C
chr7	99652769	99652770	T	
chr10	94775506	94775507	G	" > exp

gemini query -q "select chrom, start, end, ref, alt from variants" non-variants-included-snippet.db > obs
check obs exp
rm obs exp

###########################################################################
# 2. Test a query of the haplotypes table
###########################################################################
echo "    load.t2...\c"
echo "gene	name	num_variants
CACNA1S	Reference	2
CACNA1S	c.520C>T	2
CACNA1S	c.3257	2
CYP2C19	*2	1
CYP3A5	*7	1" > exp

gemini query --header -q "select gene, name, num_variants from haplotypes" non-variants-included-snippet.db > obs
check obs exp
rm obs exp

###########################################################################
# 3. Test a query of the haplotype_alleles table and join
# the haplotypes table 
###########################################################################
echo "    load.t3...\c"
echo "gene	chrom	start	end	chrom_hgvs_name	rsid	type
CACNA1S	chr1	201060814	201060815	g.201060815C>T	rs1800559	snp
CACNA1S	chr1	201091992	201091993	g.201091993G>A	rs772226819	snp" > exp

gemini query --header -q "select h.gene, a.chrom, a.start, a.end, \
a.chrom_hgvs_name, a.rsid, a.type from haplotypes h inner join haplotype_alleles a \
on h.uid = a.hap_id where h.uid = 1" non-variants-included-snippet.db > obs
check obs exp
rm obs exp

###########################################################################
# 4. Test a query of the haplotype_alleles table with match_left and 
# match_right columns 
###########################################################################
echo "    load.t4...\c"
echo "gene	name	var_id	chrom_hgvs_name	allele	type	match_left	match_right
CACNA1S	Reference	chr1_201060814	g.201060815C>T	C	snp	-1	-1
CACNA1S	Reference	chr1_201091992	g.201091993G>A	G	snp	-1	-1" > exp

gemini query --header -q "select h.gene, h.name, a.var_id, a.chrom_hgvs_name, \
a.allele, a.type, a.match_left, a.match_right from haplotypes h inner join haplotype_alleles a \
on h.uid = a.hap_id where h.uid = 1" non-variants-included-snippet.db > obs
check obs exp
rm obs exp