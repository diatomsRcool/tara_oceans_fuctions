import re
import pickle

in_file = open('/Volumes/Seagate Por/OM-RGC_seq.release.dat', 'r')

meta_file = open('environmental_metadata.txt', 'r')

out_file = open('/Volumes/Seagate Por/test_data.txt', 'w')

env = pickle.load(open('environment_dict.p', 'rb'))
gen = pickle.load(open('gene_function_dict.p', 'rb'))

miss = []
counter = 0
next(in_file)
for line in in_file:
	row = line.split(',')
	id = row[0]
	gene_id = row[1]
	kegg_id = row[3]
	m =  re.match('TARA', gene_id)
	if m != None and kegg_id != '""':
		n = re.match('TARA_\d\d\d\w{0,1}_\w\w\w_[0-9\.\-<]+', gene_id)
		sample_label = n[0]
		u = env[sample_label]
		sample_id = u[0]
		if kegg_id in gen:
			v = gen[kegg_id]
		else:
			miss.append(kegg_id)
			continue
		w = [id]
		w.append(sample_label)
		for m in u:
			w.append(m)
		w.append(kegg_id)
		for n in v:
			w.append(n)
		meta_file.seek(0)	
		for line in meta_file:
			line = line.strip('\n')
			row = line.split('\t')
			p = row[0]
			if sample_id == p:
				for x in row[1:]:
					w.append(x)
				break
			else:
				pass
	else:
		continue
	counter = counter + 1
	#print(w)	
	out_file.write('\t'.join(w) + '\n')
print(len(miss))
print(counter)