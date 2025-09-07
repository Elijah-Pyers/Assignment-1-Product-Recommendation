

# import the product database
from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.

print (products)

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

# Create an empty list to store preferences
preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list

    preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.

unique_preferences = []

unique_preferences = set(preferences)

print (unique_preferences)

# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []

for product in products:
    converted= {
        "name": product["name"],
        "tags": set(product["tags"])  # convert list -> set
    }
    converted_products.append(converted)

# Show converted products
for p in converted_products:
    print(p)


# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags["tags"] & customer_tags["tags"])
    
matches = count_matches(converted_products[0], converted_products[1])
print(f"Matching tags between {converted_products[0]['name']} and {converted_products[1]['name']}: {matches}")



# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    recommendations = []

    for product in products:
        match_count = len(product["tags"] & customer_tags)
        recommendations.append((product["name"], match_count))

    # Sort by match count (highest first), then alphabetically
    recommendations.sort(key=lambda x: (-x[1], x[0]))

    return recommendations

# TODO: Step 7 - Call your function and print the results
final_recommendations = []

final_recommendations = recommend_products(converted_products, unique_preferences)

print("\nRecommended products (sorted by relevance):")
for product, score in final_recommendations:
    print(f"{product}: {score} matching tags")


# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# 2. How might this code change if you had 1000+ products?

#DESIGN MEMO
# 1. 
# The core operation used in this code is the set intersection operator.  
# Since both customer preferences and product tags are stored as sets, intersection 
# makes it very efficient to determine common elements. This helps avoids repeated scanning 
# and also that duplicate tags are ignored automatically. I also used loops to iterate 
# over the list of products. The loop allows each product’s tag set to be compared 
# systematically against the customer’s preferences. Sorting was another important 
# operation, as it orders products by the number of matching tags. This ensures the 
# most relevant products appear first, creating a clear ranking for the user. These 
# three core operations—intersection, loops, and sorting—work together to provide a 
# straightforward recommendations.

# 2. 
# If the system had to process over 1000 products, efficiency and scalability become 
# increasingly important. Set intersections are already fast, but looping over a 
# large dataset could slow down responsiveness. To fix this, we can use list 
# sets for cleaner iteration. Additionally, we can align
# comparisons using multiprocessing to speed up execution. If 
# product data were stored in a database, indexing tags and running queries would 
# reduce the need to load all products at once. Lastly, caching frequent customer 
# queries could help deliver faster recommendations for large datasets.