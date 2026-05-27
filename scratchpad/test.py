from profam import ProFam

model = ProFam()  # loads checkpoint once (auto-downloads if needed)

# Generate sequences conditioned on family context
result = model.generate(
    prompt=["ACDEFGHIKLMNPQRSTVWY", "ACDEFGHIKLMNPQRSTVWF"],
    prompt_accessions=["seq_A", "seq_B"],  # optional: preserved in the result
    num_samples=10,
    top_p=0.95,
)
print(result.sequences)  # list of generated amino acid strings
print(result.scores)     # mean log-likelihood per sequence

print("-"*20)
result = model.score(
    sequences=["ACDEFGHIKLMNPQRSTVWY"],
    prompt=[
        "ACDEFGHIK-LMNPQRSTVWY",
        "ACDEaFGHIK-LMNPQRSTVWY",  # lowercase 'a' is an a3m-style insertion
        "ACDE-GHIK-LMNPQRSTVWY",
    ],
    use_diversity_weights=True,
)

print(result.scores)          # numpy array of mean log-likelihoods
