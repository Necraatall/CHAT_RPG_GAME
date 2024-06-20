def game_menu(character):
    menu = f"""
    [📅 Day 1, ⌚ 09:50 AM, 📌 {character.location}, 🎯 {character.current_task}, ❤️ {character.health}/20, 💎 {character.money}]
    """
    return menu

def character_journal(character):
    journal = f"""
    Name: {character.name}
    Health: {character.health}
    Money: {character.money}
    Race: {character.race}
    Class: {character.class_type}
    """
    return journal
