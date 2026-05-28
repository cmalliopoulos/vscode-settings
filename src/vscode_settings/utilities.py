import yaml
from typing import Any

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