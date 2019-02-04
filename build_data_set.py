import regex as re

in_file = open('/Volumes/Seagate Por/OM-RGC_seq.release.dat', 'r')

out_file = open('/Volumes/Seagate Por/test_data.txt', 'w')

in_file.next()
for line in in_file:
	row = line.split('\t')
	gene_id = row[1]
	kegg_id = row[3]
	m =  re.match('TARA', gene_id)
	if m != None:
		n = re.match('TARA_\d\d\d_\w\w\w_[0-9.-<]+', gene_id)
		sample_label = n[0]
		print(sample_label)