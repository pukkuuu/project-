def calculate_final_price(original_price, discount_percent, tax_percent):
    # Calculate discount amount
    discount_amount = (original_price * discount_percent) / 100
    discounted_price = original_price - discount_amount

    # Calculate tax amount
    tax_amount = (discounted_price * tax_percent) / 100
    final_price = discounted_price + tax_amount

    return final_price, discount_amount, tax_amount

def main():
    print("🛒 Discount & Tax Calculator 🏷️")

    try:
        # User Inputs
        original_price = float(input("Enter Original Price ($): "))
        discount_percent = float(input("Enter Discount Percentage (%): "))
        tax_percent = float(input("Enter Tax Percentage (%): "))

        # Validate inputs
        if original_price < 0 or discount_percent < 0 or tax_percent < 0:
            print("❌ Error: Values cannot be negative!")
            return

        # Calculate final price
        final_price, discount_amount, tax_amount = calculate_final_price(original_price, discount_percent, tax_percent)

        # Display results
        print("\n--- Calculation Summary ---")
        print(f"💰 Original Price: ${original_price:.2f}")
        print(f"🔻 Discount Applied: -${discount_amount:.2f}")
        print(f"➕ Tax Applied: +${tax_amount:.2f}")
        print(f"✅ Final Price After Discount & Tax: **${final_price:.2f}**")

    except ValueError:
        print("❌ Error: Please enter valid numerical values.")

if __name__ == "__main__":
    main()
