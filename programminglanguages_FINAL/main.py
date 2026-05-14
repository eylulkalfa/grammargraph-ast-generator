import json
import os
from grammar_reader import read_grammar
from parser_logic import Parser
from visualizer import create_parse_tree_png

def main():
    
    # Grammar 1 (Cümle yapısı/Bağlaçlar) için "1" 
    # Grammar 2 (a-b Epsilon kuralları) için "2" yapın.
    active_test = "1" 
    
    g_file = f"grammar{active_test}.txt"
    s_file = f"sentences{active_test}.txt"

    
    if not os.path.exists(g_file) or not os.path.exists(s_file):
        print(f"HATA: {g_file} veya {s_file} bulunamadı!")
        return

   
    grammar = read_grammar(g_file)
    
   
    with open(s_file, "r", encoding="utf-8") as f:
        sentences = [line.strip() for line in f if line.strip()]

    print(f"--- Grammar {active_test} Analizi Başlatıldı ---")

   
    for i, sentence in enumerate(sentences):
        print("\n" + "="*50)
        print(f"Input: {sentence}")
        
        
        if active_test == "2":
            if sentence == "ε":
                tokens = ["ε"]
            else:
                tokens = list(sentence.replace(" ", ""))
        else:
            
            tokens = sentence.split()
        
       
        parser = Parser(tokens, grammar)
        
        
        if active_test == "1":
            result_node = parser.parse_sentence()
        else:
            result_node = parser.parse_S()
        
       
        if result_node and parser.index == len(tokens):
            print("Status: Valid")
            print("\nPARSE TREE:")
            
           
            create_parse_tree_png(result_node, f"tree_output_{active_test}_sentence_{i+1}.png")
            
            
            
            print("\nJSON REPRESENTATION:")
            output_dict = {result_node.name.strip("<>"): result_node.to_dict()}
            print(json.dumps(output_dict, indent=4, ensure_ascii=False))
        
        else:
           
            print("Status: Invalid")
            print("\nError:")
            
            
            err_pos = parser.index
            found = tokens[err_pos] if err_pos < len(tokens) else "EOF (Cümle Sonu)"
            
           
            print(f" • Where the error occurs: At position {err_pos + 1} ('{found}')")
            print(f" • What was expected: {parser.expected if parser.expected else 'A valid grammar rule'}")
            print(f" • Why the sentence is invalid: {parser.reason if parser.reason else 'The sequence does not match BNF definitions'}")

if __name__ == "__main__":
    main()