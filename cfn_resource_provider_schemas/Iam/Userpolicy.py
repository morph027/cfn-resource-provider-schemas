SCHEMA = {
  "typeName" : "AWS::IAM::UserPolicy",
  "description" : "Adds or updates an inline policy document that is embedded in the specified IAM user.\n An IAM user can also have a managed policy attached to it. To attach a managed policy to a user, use [AWS::IAM::User](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html). To create a new managed policy, use [AWS::IAM::ManagedPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html). For information about policies, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html) in the *IAM User Guide*.\n For information about the maximum number of inline policies that you can embed in a user, see [IAM and quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html) in the *IAM User Guide*.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-iam.git",
  "additionalProperties" : False,
  "properties" : {
    "PolicyDocument" : {
      "description" : "The policy document.\n You must provide policies in JSON format in IAM. However, for CFN templates formatted in YAML, you can provide the policy in JSON or YAML format. CFN always converts a YAML policy to JSON format before submitting it to IAM.\n The [regex pattern](https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex) used to validate this parameter is a string of characters consisting of the following:\n  +  Any printable ASCII character ranging from the space character (``\\u0020``) through the end of the ASCII character range\n  +  The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF``)\n  +  The special characters tab (``\\u0009``), line feed (``\\u000A``), and carriage return (``\\u000D``)",
      "type" : "object"
    },
    "PolicyName" : {
      "description" : "The name of the policy document.\n This parameter allows (through its [regex pattern](https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-",
      "type" : "string"
    },
    "UserName" : {
      "description" : "The name of the user to associate the policy with.\n This parameter allows (through its [regex pattern](https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-",
      "type" : "string"
    }
  },
  "required" : [ "PolicyName", "UserName" ],
  "createOnlyProperties" : [ "/properties/PolicyName", "/properties/UserName" ],
  "primaryIdentifier" : [ "/properties/PolicyName", "/properties/UserName" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:PutUserPolicy", "iam:GetUserPolicy" ]
    },
    "read" : {
      "permissions" : [ "iam:GetUserPolicy" ]
    },
    "update" : {
      "permissions" : [ "iam:PutUserPolicy", "iam:GetUserPolicy" ]
    },
    "delete" : {
      "permissions" : [ "iam:DeleteUserPolicy", "iam:GetUserPolicy" ]
    }
  }
}