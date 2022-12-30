# Service Control Policies Deployment Automation

Deploy Service Control Policies using CDK Pipelines and GitOps integrated with AWS Access Analyzer validation tests in pull requests using GitHub Workflows with an OIDC Provider AWS IAM Role.

## Introduction
AWS Service Control Policies (SCPs) are policies that allow us to define fine-grained permissions for AWS resources within our account. They can be used to set up least privilege access, enforce compliance requirements, and prevent unintended changes to our resources. In this automation, we'll look at how we can use AWS Cloud Development Kit (CDK) and GitOps to automate the deployment and management of SCPs.

## The Idea
`Automating the Deployment of SCPs with CDK and GitOps`

One way we can use CDK to automate the deployment and management of SCPs is by using CDK Pipelines in conjunction with a GitOps model. With this approach, we can define our SCPs in code using the CDK constructs for AWS Identity and Access Management (IAM), and commit this code to a version control repository. We can then create a pipeline in CDK Pipelines to deploy the SCPs to our account.

This has several benefits:

* Automation: Changes to the SCP code in the repository will trigger a deployment through the pipeline, ensuring that our SCPs are always up to date.
* Collaboration: Using GitOps principles, we can review and approve changes to our SCPs before they are deployed, improving transparency and accountability.
* Compliance: By using a GitOps model, we can track changes to our SCPs over time and easily audit our infrastructure to ensure compliance with our policies.

To get started with this approach, we can follow these steps:

* Define our SCPs in code using the CDK constructs for IAM.
* Commit the code to our version control repository.
* Set up a pipeline in CDK Pipelines to deploy the SCPs to our account.

Enhancing the Review Process with GitHub Branch Protections and AWS Access Analyzer:

To further enhance the collaboration and review process, we add GitHub branch protections to our repository. This will require at least one review and approval from a designated team member before changes to the SCPs can be merged into the repository.

## Architecture Overview

[![Architecture Overview](https://img.youtube.com/vi/zxGmD7O2VoA/0.jpg)](https://youtu.be/zxGmD7O2VoA)

## Important Considerations
* Now that AWS has announced the ability to manage AWS Organizations using CloudFormation, this means we can build native CDK Apps to deploy AWS Organizations related automation. 
* Another big advantage is the recent announcement of delegating AWS Organizations to a member account. This means we no longer need to run any kinda of automations in the master billing account relevant to AWS Organizations, similar to our use case here of managing Service Control Policies.
* Setup an OIDC Provider along with an IAM Role with appropriate trust relationship with that provider in our AWS Account so that the specific GitHub repository can assume this role and run `aws accessanalyzer`. For this we also attach an IAM Policy with that specific permission. We provide this IAM Role ARN in our GitHub Workflow.


## Deployment & Automation Detailed Walkthrough

[![Detailed Automation Overview](https://img.youtube.com/vi/nIxZA2_Xv6g/0.jpg)](https://youtu.be/nIxZA2_Xv6g)


## Usage Instructions
* Make sure you have delegated AWS Organizations. Please follow this to get more details https://youtu.be/HgKkFoc7eRY
* Setup OIDC Provider in the AWS Account for GitHub Workflows https://youtu.be/qa9uFLqSnWY
* Establish GitHub <> AWS Developer Tools(CodePipeline) Connection using GitHub Apps https://youtu.be/qa9uFLqSnWY
* Clone this repository
  * Update `pipelines.CodePipelineSource.connection` with the GitHub Repository name and branch in the `app.py` file in root directory.
  * Update the `connection_arn` with the ARN from the AWS Developer Tools Connection settings in the same above file.
  * Update the `aws account id` and `region` in the `deploy.py` file.
  * Make changes to the Service Control Policies under the `policies` folder. 
  * If you add new policies, update the `stacks/service_control_policies_stack.py` with the appropriate code copied from existing code which deploys the current policies.
* Create a separate GitHub repository to hold all of this code, which is the one updated in `app.py`
* Push updated code to the newly created GitHub Repo.
* Deploy the CDK Pipeline using `cdk deploy`.
* Once deployment is sucessful, `CodePipeline` would automatically pull code from the new GitHub Repo and deploy the SCPs automatically :) 
* For additional enhancements, please create branch protections for the main branch, during which the GitHub Workflows will kick-in as we have configured to run during `pull-requests` for the `main` branch.


## References
https://aws.amazon.com/about-aws/whats-new/2022/11/manage-resources-aws-organizations-cloudformation/
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-policy.html
https://aws.amazon.com/about-aws/whats-new/2022/11/aws-organizations-delegated-administrator/
https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services