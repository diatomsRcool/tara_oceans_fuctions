import pickle

in_env = open('tara_oceans_sample_description.txt', 'r')
in_gene = open('functional_marker_genes.txt', 'r')

env = {}

for line in in_env:
	row = line.split('\t')
	sample_label = row[0]
	sample_id = row[4]
	date_time = row[7]
	latitude = row[8]
	longitude = row[9]
	sample_depth = row[10]
	env_feature = row[11]
	mrgid = row[15]
	d = [sample_id,date_time,latitude,longitude,sample_depth,env_feature,mrgid]
	env[sample_label] = d

fun = {}
for line in in_gene:
	row = line.split('\t')
	kegg_id = row[1]
	module = row[0]
	annotation = row[2]
	d = [module,annotation] 
	fun[kegg_id] = d

#fun['K01238'] = ['','SUN; SUN family beta-glucosidase']
#fun['K12287'] = ['biogenesis',
	
pickle.dump(env, open('environment_dict.p', 'wb'))
pickle.dump(fun, open('gene_function_dict.p', 'wb'))