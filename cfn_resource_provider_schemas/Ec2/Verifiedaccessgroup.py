SCHEMA = {
  "typeName" : "AWS::EC2::VerifiedAccessGroup",
  "description" : "The AWS::EC2::VerifiedAccessGroup resource creates an AWS EC2 Verified Access Group.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ec2-verified-access.aws-ec2-verifiedaccessgroup",
  "properties" : {
    "VerifiedAccessGroupId" : {
      "description" : "The ID of the AWS Verified Access group.",
      "type" : "string"
    },
    "VerifiedAccessInstanceId" : {
      "description" : "The ID of the AWS Verified Access instance.",
      "type" : "string"
    },
    "VerifiedAccessGroupArn" : {
      "description" : "The ARN of the Verified Access group.",
      "type" : "string"
    },
    "Owner" : {
      "description" : "The AWS account number that owns the group.",
      "type" : "string"
    },
    "CreationTime" : {
      "description" : "Time this Verified Access Group was created.",
      "type" : "string"
    },
    "LastUpdatedTime" : {
      "description" : "Time this Verified Access Group was last updated.",
      "type" : "string"
    },
    "Description" : {
      "description" : "A description for the AWS Verified Access group.",
      "type" : "string"
    },
    "PolicyDocument" : {
      "description" : "The AWS Verified Access policy document.",
      "type" : "string"
    },
    "PolicyEnabled" : {
      "description" : "The status of the Verified Access policy.",
      "type" : "boolean"
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "SseSpecification" : {
      "description" : "The configuration options for customer provided KMS encryption.",
      "$ref" : "#/definitions/SseSpecification"
    }
  },
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "SseSpecification" : {
      "description" : "The configuration options for customer provided KMS encryption.",
      "type" : "object",
      "properties" : {
        "KmsKeyArn" : {
          "description" : "KMS Key Arn used to encrypt the group policy",
          "type" : "string"
        },
        "CustomerManagedKeyEnabled" : {
          "description" : "Whether to encrypt the policy with the provided key or disable encryption",
          "type" : "boolean"
        }
      },
      "additionalProperties" : False
    }
  },
  "required" : [ "VerifiedAccessInstanceId" ],
  "additionalProperties" : False,
  "readOnlyProperties" : [ "/properties/VerifiedAccessGroupId", "/properties/CreationTime", "/properties/LastUpdatedTime", "/properties/Owner", "/properties/VerifiedAccessGroupArn" ],
  "primaryIdentifier" : [ "/properties/VerifiedAccessGroupId" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ec2:CreateTags", "ec2:DescribeTags", "ec2:DeleteTags" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:CreateVerifiedAccessGroup", "ec2:DescribeVerifiedAccessGroups", "ec2:GetVerifiedAccessGroupPolicy", "ec2:CreateTags", "ec2:DescribeTags", "kms:DescribeKey", "kms:RetireGrant", "kms:CreateGrant", "kms:GenerateDataKey", "kms:Decrypt" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeVerifiedAccessGroups", "ec2:GetVerifiedAccessGroupPolicy", "ec2:DescribeTags", "kms:DescribeKey", "kms:RetireGrant", "kms:CreateGrant", "kms:GenerateDataKey", "kms:Decrypt" ]
    },
    "update" : {
      "permissions" : [ "ec2:ModifyVerifiedAccessGroup", "ec2:ModifyVerifiedAccessGroupPolicy", "ec2:DescribeVerifiedAccessGroups", "ec2:GetVerifiedAccessGroupPolicy", "ec2:DescribeTags", "ec2:DeleteTags", "ec2:CreateTags", "kms:DescribeKey", "kms:RetireGrant", "kms:CreateGrant", "kms:GenerateDataKey", "kms:Decrypt" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DeleteVerifiedAccessGroup", "ec2:DeleteTags", "ec2:DescribeVerifiedAccessGroups", "ec2:DescribeTags", "kms:DescribeKey", "kms:RetireGrant", "kms:CreateGrant", "kms:GenerateDataKey", "kms:Decrypt" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeVerifiedAccessGroups", "ec2:DescribeTags", "kms:DescribeKey", "kms:RetireGrant", "kms:CreateGrant", "kms:GenerateDataKey", "kms:Decrypt" ]
    }
  }
}