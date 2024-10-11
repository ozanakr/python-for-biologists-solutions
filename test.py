apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
conserved_sites = [24, 56, 132]
print(apes[0])
first_site = conserved_sites[2]
chimp_index = apes.index("Pan troglodytes")
# chimp_index is now 1
last_ape = apes[-1]
ranks = ["kingdom", "phylum", "class", "order", "family"]
lower_ranks = ranks[2:5]
# lower ranks are class, order and family
apes.append("Pan paniscus")
#will add a variable at the end of the list

print("at the start : " + str(ranks))
ranks.reverse()
print("after reversing : " + str(ranks))
ranks.sort()
print("after sorting : " + str(ranks))

for ape in apes:
    print(ape)

for ape in apes:
    name_length = len(ape)
    first_letter = ape[0]
    print(ape + " is an ape. Its name starts with " + first_letter)
    print("Its name has " + str(name_length) + " letters")

names = "melanogaster,simulans,yakuba,ananassae"
species = names.split(",")
print(str(species))