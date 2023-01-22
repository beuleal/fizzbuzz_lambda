.PHONY: deploy
deploy: zip plan apply

.PHONY: destroy
destroy:
	cd iac && terraform destroy -auto-approve

# ======= Supported calls

.PHONY: zip
zip:
	zip -r fizzbuzz.zip fizzbuzz

.PHONY: plan
plan:
	cd iac && terraform init && terraform plan -out=tf.out

.PHONY: apply
apply:
	cd iac && terraform apply "tf.out"

