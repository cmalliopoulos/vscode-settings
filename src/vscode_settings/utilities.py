import yaml
from typing import Any

from json import JSONDecoder, JSONDecodeError

class MyDecoder(JSONDecoder):
    """ safe json decoder: if s is any invalid json string in decode(s), returns s.
        If s contains newlines, escapes them.
        Usage:
        json.loads(json_string, cls=MyDecoder)
    """
    def decode(self, s: str, *args, **kwargs) -> dict | str:
        slis = list(s)
        while True:
            try:
                _ = super().decode("".join(slis))
                break
            except JSONDecodeError as err:
                if slis[err.pos] == "\n":
                    # We replace with a random unicode code (without particular meaning)
                    # We cannot replace directly with "\\n" because it is 2 characters.
                    # If we want direct substitution we have to "play" with err.pos (the code becomes more involved)
                    slis[err.pos] = "\u1234"
                else: 
                    return s
        return super().decode("".join(slis).replace("\u1234", "\\n"))

class LiteralDumper(yaml.SafeDumper):
    escapes = ["\n", "\t"]

    def analyze_scalar(self, scalar):
        analysis = super().analyze_scalar(scalar)

        # Overwrite analysis.allow_block if scalar contains a control character of the above
        if any([esc in scalar for esc in self.escapes]):        
            analysis.allow_block = True
        return analysis

# Simply overiding the str representer by literal_str does not work if
# allow_block is set to False by analyse_scalar
def literal_str(dumper: LiteralDumper, value: Any):
    style = "|" if any([esc in value for esc in dumper.escapes]) else None 
    return dumper.represent_scalar("tag:yaml.org,2002:str", value, style=style)

LiteralDumper.add_representer(str, literal_str)