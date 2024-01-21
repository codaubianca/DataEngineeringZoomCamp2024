## Terraform Primer
- IaC
- human-readable config for versoning, reusinf, sharing
- consistent workflow to provision and manage all infrastructure 
#### Motivation
- simple keeping track of infrastruture
- easy to collab & reproduce
- easy resource removal
- not for deployment
### Setup
- install terrafrm in codespace/gcp
- in gcp:
    - create Service Account (IAM & Admin menu)
    - roles: Storage Admin and BigQuery Admin
### key terraform commands
init - connect to cloud provider
plan - what will happen if we apply
apply - run tf files
destroy - remove resources

### gcp notes~
ssh -i gcp codaubianca88@35.195.90.238

# TODOs
[X] set up ssh for the compute engine (see gcp docs)
[ ] install psgcli
[ ]
