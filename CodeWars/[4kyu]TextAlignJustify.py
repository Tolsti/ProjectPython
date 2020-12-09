def justify(text, width):
    line, lines = str(), list()
    
    for t in text.split():
        if len(line + t) > width:
            lines.append(line.strip())
            line = str()
        line += t + ' '
    lines.append(line.strip())
    
    for i in range(len(lines[:-1])):
        lines[i] = lines[i].split()
        while len(' '.join(lines[i])) < width and len(lines[i]) > 1:
            for j in range(len(lines[i][:-1])):
                if len(' '.join(lines[i])) < width:
                    lines[i][j] += ' '
        lines[i] = ' '.join(lines[i])
    
    return '\n'.join(lines)
