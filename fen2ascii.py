def fen_to_ascii(fen, flip=0):
    # FEN in seine 6 standardmäßigen Bestandteile zerlegen
    parts = fen.split()
    placement = parts[0]
    active_color = parts[1] if len(parts) > 1 else 'w'
    ep_square = parts[3] if len(parts) > 3 else '-'
    fullmove_number = int(parts[5]) if len(parts) > 5 else 1
    
    rows = placement.split('/')
    
    # Brett für die Ausgabe vorbereiten
    board_lines = []
    for i, row in enumerate(rows):
        rank = 8 - i
        line_content = ""
        for char in row:
            if char.isdigit():
                line_content += ". " * int(char)
            else:
                line_content += char + " "
        board_lines.append((rank, line_content.strip()))
    
    # Brett spiegeln, falls flip=1
    if flip == 1:
        board_lines.reverse()
        board_lines = [(rank, line[::-1]) for rank, line in board_lines]
    
    # ASCII-Diagramm zusammenbauen
    ascii_board = "  +-----------------+\n"
    for rank, line in board_lines:
        ascii_board += f"{rank} | {line} |\n"
    ascii_board += "  +-----------------+\n"
    
    # Koordinaten-Beschriftung anpassen
    if flip == 1:
        ascii_board += "    h g f e d c b a\n"
    else:
        ascii_board += "    a b c d e f g h\n"
        
    # Zusatz-Züge unter dem Diagramm berechnen
    info_lines = []
    
    # Prüfen, ob im letzten Zug ein Bauern-Doppelschritt stattfand
    if ep_square != '-':
        file_char = ep_square[0]
        rank_char = ep_square[1]
        
        if rank_char == '3':
            # Wenn das e.p.-Feld auf Reihe 3 liegt, hat Weiß den Doppelsschritt gemacht (z.B. e2-e4)
            info_lines.append(f"{fullmove_number}. {file_char}2-{file_char}4")
        elif rank_char == '6':
            # Wenn das e.p.-Feld auf Reihe 6 liegt, hat Schwarz den Doppelschritt gemacht (z.B. e7-e5)
            info_lines.append(f"{fullmove_number - 1}. ... {file_char}7-{file_char}5")

    # Wer ist am Zug & Fragezeichen-Zeile (Reihenfolge vertauscht)
    if active_color == 'w':
        info_lines.append("Weiß am Zug")
        info_lines.append(f"{fullmove_number}. ?")
    else:
        info_lines.append("Schwarz am Zug")
        info_lines.append(f"{fullmove_number}. ... ?")
        
    # Infos an das Diagramm anhängen
    ascii_board += "\n" + "\n".join(info_lines)
    
    return ascii_board
# Beispiel mit einer Stellung nach 1. e4 (Weiß hat gezogen, Schwarz ist am Zug)

beispiel_fen=""
while True:
    input_line=input("""FEN ?
""")
    if input_line:
        beispiel_fen=input_line
    if not beispiel_fen:
        continue
    flip_board= 1 if input("flip board? y/N") else 0
    print(fen_to_ascii(beispiel_fen, flip_board))

