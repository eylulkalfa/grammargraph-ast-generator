from nodes import Node

class Parser:
    def __init__(self, tokens, grammar):
        self.tokens = tokens
        self.grammar = grammar
        self.index = 0
       
        self.expected = ""
        self.reason = ""

    def get_current(self):
        if self.index < len(self.tokens):
            return self.tokens[self.index]
        return None

   
    def set_error(self, expected, reason):
       
        if not self.expected:
            self.expected = expected
            self.reason = reason

    def parse_sentence(self):
        node = Node("<sentence>")
        np = self.parse_noun_phrase()
        if np:
            vp = self.parse_verb_phrase()
            if vp:
                node.add_child(np)
                node.add_child(vp)
                return node
           
            self.set_error("a verb phrase", "The sentence has a subject but lacks a predicate/verb.")
        else:
            self.set_error("a noun phrase (starting with 'the' or 'a')", "Grammar requires a noun phrase at the beginning of the sentence.")
        return None

    def parse_noun_phrase(self):
        node = Node("<noun-phrase>")
        save_index = self.index
        
        pronoun = self.parse_pronoun()
        if pronoun:
            node.add_child(pronoun)
            return node
        
        self.index = save_index
        det = self.parse_determiner()
        if det:
            node.add_child(det)
            adj_list = self.parse_adjective_list()
            node.add_child(adj_list)
            nl = self.parse_noun_list()
            if nl:
                node.add_child(nl)
                return node
            self.set_error("a noun", f"After a determiner/adjective, a noun is required.")
        return None

    def parse_noun_list(self):
        node = Node("<noun-list>")
        n1 = self.parse_noun()
        if n1:
            node.add_child(n1)
            save_index = self.index
            conj = self.parse_conjunction()
            if conj:
                node.add_child(conj)
                n2 = self.parse_noun()
                if n2:
                    node.add_child(n2)
                else:
                    self.index = save_index
                    node.children.pop()
            return node
        return None

    def parse_verb_phrase(self):
        node = Node("<verb-phrase>")
        verb = self.parse_verb()
        if verb:
            node.add_child(verb)
            save_index = self.index
            np = self.parse_noun_phrase()
            if not np:
                self.index = save_index
            else:
                node.add_child(np)
            node.add_child(self.parse_adverb_list())
            return node
        return None

   
    def parse_determiner(self):
        t = self.get_current()
        if t and any(t in opts for opts in self.grammar.get('<determiner>', [])):
            self.index += 1; return Node("<determiner>", t)
        return None

    def parse_noun(self):
        t = self.get_current()
        if t and any(t in opts for opts in self.grammar.get('<noun>', [])):
            self.index += 1; return Node("<noun>", t)
        return None

    def parse_verb(self):
        t = self.get_current()
        if t and any(t in opts for opts in self.grammar.get('<verb>', [])):
            self.index += 1; return Node("<verb>", t)
        return None

    def parse_pronoun(self):
        t = self.get_current()
        if t and any(t in opts for opts in self.grammar.get('<pronoun>', [])):
            self.index += 1; return Node("<pronoun>", t)
        return None

    def parse_conjunction(self):
        t = self.get_current()
        if t and any(t in opts for opts in self.grammar.get('<conjunction>', [])):
            self.index += 1; return Node("<conjunction>", t)
        return None

    def parse_adjective(self):
        t = self.get_current()
        if t and any(t in opts for opts in self.grammar.get('<adjective>', [])):
            self.index += 1; return Node("<adjective>", t)
        return None

    def parse_adverb(self):
        t = self.get_current()
        if t and any(t in opts for opts in self.grammar.get('<adverb>', [])):
            self.index += 1; return Node("<adverb>", t)
        return None

    def parse_adjective_list(self):
        node = Node("<adjective-list>")
        adj = self.parse_adjective()
        if adj: node.add_child(adj)
        else: node.add_child(Node("ε", "empty"))
        return node

    def parse_adverb_list(self):
        node = Node("<adverb-list>")
        adv = self.parse_adverb()
        if adv: node.add_child(adv)
        else: node.add_child(Node("ε", "empty"))
        return node

   
    def parse_S(self):
        node = Node("<S>")
        node.add_child(self.parse_A())
        node.add_child(self.parse_B())
        return node

    def parse_A(self):
        node = Node("<A>"); t = self.get_current()
        if t == 'a':
            node.add_child(Node("a", t)); self.index += 1
            node.add_child(self.parse_A()); return node
        if t == 'ε': self.index += 1
        node.add_child(Node("ε", "empty")); return node

    def parse_B(self):
        node = Node("<B>"); t = self.get_current()
        if t == 'b':
            node.add_child(Node("b", t)); self.index += 1
            node.add_child(self.parse_B()); return node
        if t == 'ε': self.index += 1
        node.add_child(Node("ε", "empty")); return node