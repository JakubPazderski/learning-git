shopping_list=["chleb","bułki","pączki","marchew","ogórek","rukola"]
shopping_dict={
    "piekarnia":[shopping_list[0].capitalize(),shopping_list[1].capitalize(),shopping_list[2].capitalize()],
    "warzywniak":[shopping_list[3].capitalize(), shopping_list[4].capitalize(), shopping_list[5].capitalize()]
}
for shop,products in shopping_dict.items():
    print (f"Wchodzę do {shop.capitalize()} i kupuję {products}.")
print (f"W sumie kupuję {len(shopping_list)} produktów.")
for shop, products in shopping_dict.items():
    print (f"W {shop.capitalize()} kupuję {len(products)} produkty")
