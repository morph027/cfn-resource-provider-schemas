SCHEMA = {
  "typeName" : "AWS::IAM::ManagedPolicy",
  "description" : "Creates a new managed policy for your AWS-account.\n This operation creates a policy version with a version identifier of ``v1`` and sets v1 as the policy's default version. For more information about policy versions, see [Versioning for managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html) in the *IAM User Guide*.\n As a best practice, you can validate your IAM policies. To learn more, see [Validating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_policy-validator.html) in the *IAM User Guide*.\n For more information about managed policies in general, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html) in the *IAM User Guide*.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-iam",
  "additionalProperties" : False,
  "properties" : {
    "Description" : {
      "type" : "string",
      "description" : "A friendly description of the policy.\n Typically used to store information about the permissions defined in the policy. For example, \"Grants access to production DynamoDB tables.\"\n The policy description is immutable. After a value is assigned, it cannot be changed."
    },
    "Groups" : {
      "insertionOrder" : False,
      "type" : "array",
      "description" : "The name (friendly name, not ARN) of the group to attach the policy to.\n This parameter allows (through its [regex pattern](https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-",
      "uniqueItems" : True,
      "items" : {
        "type" : "string"
      }
    },
    "ManagedPolicyName" : {
      "type" : "string",
      "description" : "The friendly name of the policy.\n  If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.\n  If you specify a name, you must specify the ``CAPABILITY_NAMED_IAM`` value to acknowledge your template's capabilities. For more information, see [Acknowledging Resources in Templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities).\n  Naming an IAM resource can cause an unrecoverable error if you reuse the same template in multiple Regions. To prevent this, we recommend using ``Fn::Join`` and ``AWS::Region`` to create a Region-specific name, as in the following example: ``{\"Fn::Join\": [\"\", [{\"Ref\": \"AWS::Region\"}, {\"Ref\": \"MyResourceName\"}]]}``."
    },
    "Path" : {
      "type" : "string",
      "default" : "/",
      "description" : "The path for the policy.\n For more information about paths, see [IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.\n This parameter is optional. If it is not included, it defaults to a slash (/).\n This parameter allows (through its [regex pattern](https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (``\\u0021``) through the DEL character (``\\u007F``), including most punctuation characters, digits, and upper and lowercased letters.\n  You cannot use an asterisk (*) in the path name."
    },
    "PolicyDocument" : {
      "type" : [ "object", "string" ],
      "description" : "The JSON policy document that you want to use as the content for the new policy.\n You must provide policies in JSON format in IAM. However, for CFN templates formatted in YAML, you can provide the policy in JSON or YAML format. CFN always converts a YAML policy to JSON format before submitting it to IAM.\n The maximum length of the policy document that you can pass in this operation, including whitespace, is listed below. To view the maximum character counts of a managed policy with no whitespaces, see [IAM and character quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-entity-length).\n To learn more about JSON policy grammar, see [Grammar of the IAM JSON policy language](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_grammar.html) in the *IAM User Guide*. \n The [regex pattern](https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex) used to validate this parameter is a string of characters consisting of the following:\n  +  Any printable ASCII character ranging from the space character (``\\u0020``) through the end of the ASCII character range\n  +  The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF``)\n  +  The special characters tab (``\\u0009``), line feed (``\\u000A``), and carriage return (``\\u000D``)"
    },
    "Roles" : {
      "insertionOrder" : False,
      "type" : "array",
      "description" : "The name (friendly name, not ARN) of the role to attach the policy to.\n This parameter allows (per its [regex pattern](https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-\n  If an external policy (such as ``AWS::IAM::Policy`` or ``AWS::IAM::ManagedPolicy``) has a ``Ref`` to a role and if a resource (such as ``AWS::ECS::Service``) also has a ``Ref`` to the same role, add a ``DependsOn`` attribute to the resource to make the resource depend on the external policy. This dependency ensures that the role's policy is available throughout the resource's lifecycle. For example, when you delete a stack with an ``AWS::ECS::Service`` resource, the ``DependsOn`` attribute ensures that CFN deletes the ``AWS::ECS::Service`` resource before deleting its role's policy.",
      "uniqueItems" : True,
      "items" : {
        "type" : "string"
      }
    },
    "Users" : {
      "insertionOrder" : False,
      "type" : "array",
      "description" : "The name (friendly name, not ARN) of the IAM user to attach the policy to.\n This parameter allows (through its [regex pattern](https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-",
      "uniqueItems" : True,
      "items" : {
        "type" : "string"
      }
    },
    "PolicyArn" : {
      "type" : "string",
      "description" : ""
    },
    "AttachmentCount" : {
      "type" : "integer",
      "description" : ""
    },
    "CreateDate" : {
      "type" : "string",
      "description" : ""
    },
    "UpdateDate" : {
      "type" : "string",
      "description" : ""
    },
    "DefaultVersionId" : {
      "type" : "string",
      "description" : ""
    },
    "IsAttachable" : {
      "type" : "boolean",
      "description" : ""
    },
    "PermissionsBoundaryUsageCount" : {
      "type" : "integer",
      "description" : ""
    },
    "PolicyId" : {
      "type" : "string",
      "description" : ""
    }
  },
  "required" : [ "PolicyDocument" ],
  "createOnlyProperties" : [ "/properties/ManagedPolicyName", "/properties/Description", "/properties/Path" ],
  "readOnlyProperties" : [ "/properties/PolicyArn", "/properties/AttachmentCount", "/properties/CreateDate", "/properties/DefaultVersionId", "/properties/IsAttachable", "/properties/PermissionsBoundaryUsageCount", "/properties/PolicyId", "/properties/UpdateDate" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "primaryIdentifier" : [ "/properties/PolicyArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:CreatePolicy", "iam:AttachGroupPolicy", "iam:AttachUserPolicy", "iam:AttachRolePolicy" ]
    },
    "read" : {
      "permissions" : [ "iam:GetPolicy", "iam:ListEntitiesForPolicy", "iam:GetPolicyVersion" ]
    },
    "update" : {
      "permissions" : [ "iam:DetachRolePolicy", "iam:GetPolicy", "iam:ListPolicyVersions", "iam:DetachGroupPolicy", "iam:DetachUserPolicy", "iam:CreatePolicyVersion", "iam:DeletePolicyVersion", "iam:AttachGroupPolicy", "iam:AttachUserPolicy", "iam:AttachRolePolicy" ]
    },
    "delete" : {
      "permissions" : [ "iam:DetachRolePolicy", "iam:GetPolicy", "iam:ListPolicyVersions", "iam:DetachGroupPolicy", "iam:DetachUserPolicy", "iam:DeletePolicyVersion", "iam:DeletePolicy", "iam:ListEntitiesForPolicy" ]
    },
    "list" : {
      "permissions" : [ "iam:ListPolicies" ]
    }
  }
}