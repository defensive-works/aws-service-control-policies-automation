from aws_cdk import (
	Stack,
	aws_organizations as organizations
)

from constructs import Construct

class AutomatedSCPStack(Stack):

	def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
		super().__init__(scope, construct_id, **kwargs)

		# Policy for restricting or disabling unused AWS Regions
		with open('policies/deny-actions-outside-approved-regions.json', 'r') as f:
			deny_actions_outside_approved_regions_policy = f.read()

		deny_actions_outside_approved_regions_policy = organizations.CfnPolicy(
			self, 'deny_actions_outside_approved_regions_policy',
			content=deny_actions_outside_approved_regions_policy,
			name='deny-actions-outside-approved-regions',
			type='SERVICE_CONTROL_POLICY',
			description='Restrict unapproved regions.',
			target_ids=['946996879141']
		)

		# Policy for restricting the creation of IAM Users/Access Keys
		with open('policies/deny-ability-to-create-iam-access-keys-users.json', 'r') as f:
			deny_ability_to_create_iam_access_keys_users_policy = f.read()

		deny_manual_changes_identity_center_policy = organizations.CfnPolicy(
			self, 'deny_ability_to_create_iam_access_keys_users_policy',
			content=deny_ability_to_create_iam_access_keys_users_policy,
			name='deny-ability-to-create-iam-access-keys-users',
			type='SERVICE_CONTROL_POLICY',
			description='Restrict users the ability to create IAM access keys or users',
			target_ids=['ou-g63m-8pshnzfy']
		)		