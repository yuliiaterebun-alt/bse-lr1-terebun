def calculate_printing_cost(pages, copies, cost_per_page=0.5):
    """
    Програма для розрахунку базової вартості друку тиражу.
    """
    total_pages = pages * copies
    total_cost = total_pages * cost_per_page
    return total_pages, total_cost

if __name__ == "__main__":
    print("--- Програма розрахунку видавничого тиражу ---")
    
    # Вхідні дані для тесту
    pages_count = 120    # кількість сторінок у книзі
    copies_count = 500   # тираж (кількість примірників)
    
    pages, cost = calculate_printing_cost(pages_count, copies_count)
    
    print(f"Кількість сторінок у книзі: {pages_count}")
    print(f"Загальний тираж: {copies_count} прим.")
    print(f"Загальна кількість сторінок для друку: {pages} стор.")
    print(f"Орієнтовна вартість друку: {cost} грн.")