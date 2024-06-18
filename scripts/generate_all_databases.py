import scripts.generate_databaseCLD as dbCLD
import scripts.generate_databaseCSD as dbCSD
import scripts.generate_databaseHTD as dbHTD
import scripts.generate_databaseLBP as dbLBP

IMAGE_DIR = '../base_imgs_testes/'


# Generate the databases
print('Generating databases...')
dbCLD.GenerateDatabaseCLD(IMAGE_DIR).generate_database()
print('CLD Done!')
dbCSD.GenerateDatabaseCSD(IMAGE_DIR).generate_database()
print('CSD Done!')
dbHTD.GenerateDatabaseHTD(IMAGE_DIR).generate_database()
print('HTD Done!')
dbLBP.GenerateDatabaseLBP(IMAGE_DIR).generate_database()
print('LBP Done!')
print('All databases generated!')
