SCHEMA = {
  "typeName" : "AWS::IAM::RolePolicy",
  "description" : "Adds or updates an inline policy document that is embedded in the specified IAM role.\n When you embed an inline policy in a role, the inline policy is used as part of the role's access (permissions) policy. The role's trust policy is created at the same time as the role, using [CreateRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html). You can update a role's trust policy using [UpdateAssumeRolePolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateAssumeRolePolicy.html). For information about roles, see [roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html) in the *IAM User Guide*.\n A role can also have a managed policy attached to it. To attach a managed policy to a role, use [AWS::IAM::Role](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html). To create a new managed policy, use [AWS::IAM::ManagedPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html). For information about policies, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html) in the *IAM User Guide*.\n For information about the maximum number of inline policies that you can embed with a role, see [IAM and quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html) in the *IAM User Guide*.",
  "additionalProperties" : False,
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-iam.git",
  "properties" : {
    "PolicyDocument" : {
      "description" : "The policy document.\n You must provide policies in JSON format in IAM. However, for CFN templates formatted in YAML, you can provide the policy in JSON or YAML format. CFN always converts a YAML policy to JSON format before submitting it to IAM.\n The [regex pattern](https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex) used to validate this parameter is a string of characters consisting of the following:\n  +  Any printable ASCII character ranging from the space character (``\\u0020``) through the end of the ASCII character range\n  +  The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF``)\n  +  The special characters tab (``\\u0009``), line feed (``\\u000A``), and carriage return (``\\u000D``)",
      "type" : "object"
    },
    "PolicyName" : {
      "description" : "The name of the policy document.\n This parameter allows (through its [regex pattern](https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-",
      "type" : "string"
    },
    "RoleName" : {
      "description" : "The name of the role to associate the policy with.\n This parameter allows (through its [regex pattern](https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-",
      "type" : "string"
    }
  },
  "required" : [ "PolicyName", "RoleName" ],
  "primaryIdentifier" : [ "/properties/PolicyName", "/properties/RoleName" ],
  "createOnlyProperties" : [ "/properties/PolicyName", "/properties/RoleName" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:PutRolePolicy", "iam:GetRolePolicy" ]
    },
    "read" : {
      "permissions" : [ "iam:GetRolePolicy" ]
    },
    "update" : {
      "permissions" : [ "iam:PutRolePolicy", "iam:GetRolePolicy" ]
    },
    "delete" : {
      "permissions" : [ "iam:DeleteRolePolicy", "iam:GetRolePolicy" ]
    }
  }
}