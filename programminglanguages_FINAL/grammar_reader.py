def read_grammar(file_path):
    grammar_dict = {}
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if "::=" in line: # Kural satırı mı? [cite: 47]
                lhs, rhs = line.split("::=")
                lhs = lhs.strip()
                # Seçenekleri ayır (cat | dog) [cite: 45]
                options = [opt.strip().split() for opt in rhs.split("|")]
                grammar_dict[lhs] = options
    return grammar_dict