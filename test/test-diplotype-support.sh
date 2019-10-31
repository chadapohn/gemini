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
gemini load -v non-variants-included-snippet.vcf \
--skip-gene-tables --skip-gerp-bp --skip-cadd non-variants-included-snippet.db

echo "    load.t1...\c"
echo "chr1	96078437	96078438	A	
chr1	96078438	96078439	T	C" > exp

gemini query -q "select chrom, start, end, ref, alt from variants" non-variants-included-snippet.db > obs
check obs exp
rm obs exp

###########################################################################
# 2. Test a query of the haplotypes table
###########################################################################
echo "    load.t2...\c"
echo "uid	gene	name	num_variants
1	CAC1NAS	Reference	2
2	CAC1NAS	c.520C>T	2
3	CAC1NAS	c.3257	2" > exp

gemini query --header -q "select uid, gene, name, num_variants from haplotypes limit 3" non-variants-included-snippet.db > obs
check obs exp
rm obs exp

###########################################################################
# 3. Test a query of the phased_data_haplotype_alleles table and join
# the haplotypes table 
###########################################################################
echo "    load.t3...\c"
echo "gene	start	end	chrom_hgvs_name	rsid	type
CAC1NAS	201060814	201060815	g.201060815C>T	rs1800559	snp
CAC1NAS	201091992	201091993	g.201091993G>A	rs772226819	snp" > exp

gemini query --header -q "select h.gene, a.start, a.end, \
a.chrom_hgvs_name, a.rsid, a.type from haplotypes h inner join phased_data_haplotype_alleles a \
on h.uid = a.hap_id where h.uid = 1" non-variants-included-snippet.db > obs
check obs exp
rm obs exp