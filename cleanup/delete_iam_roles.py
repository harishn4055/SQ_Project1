import boto3

# Initialize the AWS IAM client
iam_client = boto3.client('iam')

def delete_iam_role(role_name):
    """
    Delete an IAM role by its name.
    """
    try:
        # Detach all policies attached to the role
        attached_policies = iam_client.list_attached_role_policies(RoleName=role_name)
        for policy in attached_policies['AttachedPolicies']:
            iam_client.detach_role_policy(
                RoleName=role_name,
                PolicyArn=policy['PolicyArn']
            )
            print(f"Detached policy {policy['PolicyArn']} from role {role_name}")

        # Delete any inline policies
        inline_policies = iam_client.list_role_policies(RoleName=role_name)
        for policy_name in inline_policies['PolicyNames']:
            iam_client.delete_role_policy(
                RoleName=role_name,
                PolicyName=policy_name
            )
            print(f"Deleted inline policy {policy_name} from role {role_name}")

        # Delete the role
        response = iam_client.delete_role(RoleName=role_name)
        print(f"IAM role '{role_name}' deleted successfully.")
        print(response)
    except Exception as e:
        print(f"Error deleting IAM role '{role_name}': {e}")

if __name__ == "__main__":
    # List of IAM roles to delete
    iam_roles = [
        'LambdaExecutionRole'  
    ]
    
    for role_name in iam_roles:
        delete_iam_role(role_name)
