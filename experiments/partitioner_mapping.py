#!/usr/bin/python3
from typing import List

class Partitioner:
    def __init__(
        self,
        script: str,
        format: str | List[str],
        *,
        parallel: bool,
        dynamic_header: bool = False,
    ) -> None:
        self.script = script
        if isinstance(format, str):
            self.format = [format]
        else:
            self.format = format
        self.parallel = parallel
        self.dynamic_header = dynamic_header


partitioner_mapping = {
    "Mt-KaHyPar":       Partitioner("mt_kahypar", ["graph", "hmetis"], parallel=True, dynamic_header=True),
    "hMetis-R":         Partitioner("hmetis_rb", "hmetis", parallel=False),
    "hMetis-K":         Partitioner("hmetis_k", "hmetis", parallel=False),
    "PaToH-S":          Partitioner("patoh_s", "patoh", parallel=False),
    "PaToH-D":          Partitioner("patoh_d", "patoh", parallel=False),
    "PaToH-Q":          Partitioner("patoh_q", "patoh", parallel=False),
    "KaHyPar-CA":       Partitioner("kahypar_ca", "hmetis", parallel=False),
    "KaHyPar-K":        Partitioner("kahypar_k", "hmetis", parallel=False),
    "KaHyPar-R":        Partitioner("kahypar_r", "hmetis", parallel=False),
    "Parkway":          Partitioner("parkway", "hmetis", parallel=True),
    "Zoltan":           Partitioner("zoltan", "zoltan", parallel=True),
    "BiPart":           Partitioner("bipart", "hmetis", parallel=True),
    "MT-KaHIP":         Partitioner("mt_kahip", "graph", parallel=True),
    "MT-Metis":         Partitioner("mt_metis", "graph", parallel=True),
    "KaMinPar":         Partitioner("kaminpar", "graph", parallel=True),
    "Metis-R":          Partitioner("metis_rb", "graph", parallel=False),
    "Metis-K":          Partitioner("metis_k", "graph", parallel=False),
    "Scotch":           Partitioner("scotch", "scotch", parallel=False),
    "PT-Scotch":        Partitioner("pt_scotch", "scotch", parallel=True),
    "KaFFPa-Fast":      Partitioner("kaffpa_fast", "graph", parallel=False),
    "KaFFPa-FastS":     Partitioner("kaffpa_fastsocial", "graph", parallel=False),
    "KaFFPa-Eco":       Partitioner("kaffpa_eco", "graph", parallel=False),
    "KaFFPa-EcoS":      Partitioner("kaffpa_ecosocial", "graph", parallel=False),
    "KaFFPa-Strong":    Partitioner("kaffpa_strong", "graph", parallel=False),
    "KaFFPa-StrongS":   Partitioner("kaffpa_strongsocial", "graph", parallel=False),
    "ParHIP":           Partitioner("parhip", "graph", parallel=True),
    "ParMetis":         Partitioner("parmetis", "graph", parallel=True),
}
