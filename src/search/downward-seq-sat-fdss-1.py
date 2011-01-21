#! /usr/bin/env python2.6
# -*- coding: utf-8 -*-

import seq_sat_portfolio

# NOTE: when using iterated search included, we must include the option
#       "plan_counter=PLANCOUNTER"

CONFIGS = [
    # alt_lazy_ff_cg
    (49, ["--heuristic", "hff=ff(cost_type=1)",
         "--heuristic", "hcg=cg(cost_type=1)", "--search",
         "lazy_greedy(hff,hcg,preferred=(hff,hcg),cost_type=1,bound=BOUND)"]),
    # lazy_greedy_ff_1
    (171, ["--heuristic", "h=ff(cost_type=1)",
          "--search",
          "lazy_greedy(h,preferred=(h),cost_type=0,bound=BOUND)"]),
    # alt_lazy_cea_cg
    (27, ["--heuristic", "hcea=cea(cost_type=1)", 
         "--heuristic", "hcg=cg(cost_type=1)", "--search",
         "lazy_greedy(hcea,hcg,preferred=(hcea,hcg),cost_type=1,bound=BOUND)"]),
    # lazy_wa3_ff_1
    (340, ["--heuristic", "h=ff(cost_type=1)",
          "--search",
          "lazy_wastar(h,w=3,preferred=(h),cost_type=1,bound=BOUND)"]),
    # alt_eager_ff_cg
    (76, ["--heuristic", "hff=ff(cost_type=1)",
         "--heuristic", "hcg=cg(cost_type=1)", "--search",
         "eager_greedy(hff,hcg,preferred=(hff,hcg),cost_type=1,bound=BOUND)"]),
    # eager_greedy_ff_1
    (88, ["--heuristic", "h=ff(cost_type=1)",
          "--search",
          "eager_greedy(h,preferred=(h),cost_type=0,bound=BOUND)"]),
    # alt_eager_ff_add
    (90, ["--heuristic", "hff=ff(cost_type=1)",
         "--heuristic", "hadd=add(cost_type=1)", "--search",
         "eager_greedy(hff,hadd,preferred=(hff,hadd),cost_type=1,bound=BOUND)"]), 
    # lazy_greedy_cea_1
    (56, ["--heuristic", "h=cea(cost_type=1)",
          "--search",
          "lazy_greedy(h,preferred=(h),cost_type=0,bound=BOUND)"]),
    # alt_eager_ff_cea_cg
    (73, ["--heuristic", "hff=ff(cost_type=1)",
          "--heuristic", "hcea=cea(cost_type=1)",
          "--heuristic", "hcg=cg(cost_type=1)",
          "--search",
          "eager_greedy(hff,hcea,hcg,preferred=(hff,hcea,hcg),cost_type=1,bound=BOUND)"]),
    # lazy_wa3_add_1
    (50, ["--heuristic", "h=add(cost_type=1)",
          "--search",
          "lazy_wastar(h,w=3,preferred=(h),cost_type=0,bound=BOUND)"]),
    # eager_greedy_cea_1
    (84, ["--heuristic", "h=cea(cost_type=1)",
          "--search",
          "eager_greedy(h,preferred=(h),cost_type=0,bound=BOUND)"]),
    # eager_wa3_add_1
    (166, ["--heuristic", "h=add(cost_type=1)",
          "--search",
          "eager(single(sum(g(),weight(h,3))),preferred=(h),cost_type=0,bound=BOUND)"]),
    # eager_wa3_ff_1
    (87, ["--heuristic", "h=ff(cost_type=1)",
          "--search",
          "eager(single(sum(g(),weight(h,3))),preferred=(h),cost_type=1,bound=BOUND)"]),
    # lazy_wa3_cg_1
    (73, ["--heuristic", "h=cg(cost_type=1)",
         "--search",
         "lazy_wastar(h,w=3,preferred=(h),cost_type=0,bound=BOUND)"]),
    # eager_wa3_cg_1
    (89, ["--heuristic", "h=cg(cost_type=1)",
          "--search",
          "eager(single(sum(g(),weight(h,3))),preferred=(h),cost_type=0,bound=BOUND)"]),
     ]

NONUNIT_CONFIGS = [
    (91, ["--heuristic", "hff=ff(cost_type=1)",
         "--heuristic", "hcg=cg(cost_type=1)", "--search",
         "eager_greedy(hff,hcg,preferred=(hff,hcg),cost_type=1,bound=BOUND)"]),
    (89, ["--heuristic", "hadd=add(cost_type=1)", "--heuristic",
        "hcg=cg(cost_type=1)", "--search",
        "lazy_greedy(hadd,hcg,preferred=(hadd,hcg),cost_type=1,bound=BOUND)"]),
    (82, ["--heuristic", "hadd=add(cost_type=1)",
          "--heuristic", "hcg=cg(cost_type=1)",
          "--search",
          "eager_greedy(hadd,hcg,preferred=(hadd,hcg),cost_type=1,bound=BOUND)"]),
    (30, ["--heuristic", "h=cg(cost_type=1)",
          "--search",
          "eager_greedy(h,preferred=(h),cost_type=0,bound=BOUND)"]),
    (79, ["--heuristic", "h=cg(cost_type=1)",
          "--search",
          "eager(single(sum(g(),weight(h,3))),preferred=(h),cost_type=0,bound=BOUND)"]),
    (105, ["--heuristic", "h=ff(cost_type=1)",
          "--search",
          "eager(single(sum(g(),weight(h,3))),preferred=(h),cost_type=1,bound=BOUND)"]),
    (356, ["--heuristic", "h=cg(cost_type=1)",
          "--search",
          "lazy_greedy(h,preferred=(h),cost_type=0,bound=BOUND)"]),
    (104, ["--heuristic", "h=add(cost_type=1)",
          "--search",
          "lazy_wastar(h,w=3,preferred=(h),cost_type=0,bound=BOUND)"]),
    (37, ["--heuristic", "h=add(cost_type=1)",
          "--search",
          "lazy_wastar(h,w=3,preferred=(h),cost_type=1,bound=BOUND)"]),
    (93, ["--heuristic", "h=ff(cost_type=1)",
          "--search",
          "lazy_wastar(h,w=3,preferred=(h),cost_type=1,bound=BOUND)"]),
    (139, ["--heuristic", "h=ff(cost_type=1)",
          "--search",
          "lazy_wastar(h,w=3,preferred=(h),cost_type=0,bound=BOUND)"]),
     ]

UNIT_CONFIGS = [
    (106, ["--heuristic", "hff=ff(cost_type=1)",
          "--heuristic", "hadd=add(cost_type=1)",
          "--search",
          "eager_greedy(hff,hadd,preferred=(hff,hadd),cost_type=1,bound=BOUND)"]),
    (117, ["--heuristic", "hff=ff(cost_type=1)",
          "--heuristic", "hcea=cea(cost_type=1)",
          "--heuristic", "hcg=cg(cost_type=1)",
          "--search",
          "eager_greedy(hff,hcea,hcg,preferred=(hff,hcea,hcg),cost_type=1,bound=BOUND)"]),
    (50, ["--heuristic", "hff=ff(cost_type=1)",
          "--heuristic", "hcea=cea(cost_type=1)",
          "--heuristic", "hcg=cg(cost_type=1)",
          "--search",
          "lazy_greedy(hff,hcea,hcg,preferred=(hff,hcea,hcg),cost_type=1,bound=BOUND)"]),
    (213, ["--heuristic", "h=cea(cost_type=1)",
          "--search",
          "eager_greedy(h,preferred=(h),cost_type=0,bound=BOUND)"]),
    (93, ["--heuristic", "h=cg(cost_type=1)",
          "--search",
          "eager_greedy(h,preferred=(h),cost_type=0,bound=BOUND)"]),
    (94, ["--heuristic", "h=add(cost_type=1)",
          "--search",
          "eager(single(sum(g(),weight(h,3))),preferred=(h),cost_type=0,bound=BOUND)"]),
    (98, ["--heuristic", "h=ff(cost_type=1)",
         "--search",
         "eager(single(sum(g(),weight(h,3))),preferred=(h),cost_type=0,bound=BOUND)"]),
    (57, ["--heuristic", "h=cea(cost_type=1)",
          "--search",
          "lazy_greedy(h,preferred=(h),cost_type=0,bound=BOUND)"]),
    (111, ["--heuristic", "h=ff(cost_type=1)",
          "--search",
          "lazy_greedy(h,preferred=(h),cost_type=0,bound=BOUND)"]),
    (65, ["--heuristic", "h=cea(cost_type=1)",
         "--search",
         "lazy_wastar(h,w=3,preferred=(h),cost_type=0,bound=BOUND)"]),
    (88, ["--heuristic", "h=cg(cost_type=1)",
         "--search",
         "lazy_wastar(h,w=3,preferred=(h),cost_type=0,bound=BOUND)"]),
    (340, ["--heuristic", "h=ff(cost_type=1)",
         "--search",
         "lazy_wastar(h,w=3,preferred=(h),cost_type=0,bound=BOUND)"]),
     ]

seq_sat_portfolio.run(unit_configs=CONFIGS,
                      nonunit_configs=CONFIGS)