#!/usr/bin/python3
import os
import os.path

from mt_kahypar_common import (get_args, invalid, parse_or_default,
                               parse_required_value, print_call, print_result,
                               run_mtkahypar, set_result_vals)

###################################
# SETUP ENV
###################################
algorithm = "Mt-KaHyPar"
mt_kahypar = os.environ.get("MT_KAHYPAR")
assert (mt_kahypar != None), "check env.sh"
###################################

args = get_args()
if args.name != "":
  algorithm = args.name

# for debugging: replace run_mtkahypar with print_call
result, success = run_mtkahypar(mt_kahypar, args, default_args={
  "--preset-type": "default",
}, detect_instance_type=True)

set_result_vals(
  km1=invalid,
  cut=invalid,
  total_time=invalid,
  imbalance=1.0,
)
if success:
  parse_required_value(result, "km1", parser=int)
  parse_required_value(result, "cut", parser=int)
  parse_required_value(result, "totalPartitionTime", out="total_time")
  parse_required_value(result, "imbalance")

if success is not None:
  print_result(algorithm, args)
