SCHEMA = {
  "typeName" : "AWS::Organizations::Organization",
  "description" : "Resource schema for AWS::Organizations::Organization",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-organizations.git",
  "properties" : {
    "Id" : {
      "description" : "The unique identifier (ID) of an organization.",
      "type" : "string",
      "pattern" : "^o-[a-z0-9]{10,32}$"
    },
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) of an organization.",
      "type" : "string",
      "pattern" : "^arn:aws.*:organizations::\\d{12}:organization\\/o-[a-z0-9]{10,32}"
    },
    "FeatureSet" : {
      "description" : "Specifies the feature set supported by the new organization. Each feature set supports different levels of functionality.",
      "type" : "string",
      "enum" : [ "ALL", "CONSOLIDATED_BILLING" ],
      "default" : "ALL"
    },
    "ManagementAccountArn" : {
      "description" : "The Amazon Resource Name (ARN) of the account that is designated as the management account for the organization.",
      "type" : "string",
      "pattern" : "^arn:aws.*:organizations::\\d{12}:account\\/o-[a-z0-9]{10,32}\\/\\d{12}"
    },
    "ManagementAccountId" : {
      "description" : "The unique identifier (ID) of the management account of an organization.",
      "type" : "string",
      "pattern" : "^\\d{12}$"
    },
    "ManagementAccountEmail" : {
      "description" : "The email address that is associated with the AWS account that is designated as the management account for the organization.",
      "type" : "string",
      "pattern" : "[^\\s@]+@[^\\s@]+\\.[^\\s@]+",
      "minLength" : 6,
      "maxLength" : 64
    },
    "RootId" : {
      "description" : "The unique identifier (ID) for the root.",
      "type" : "string",
      "pattern" : "^r-[0-9a-z]{4,32}$",
      "maxLength" : 64
    }
  },
  "tagging" : {
    "taggable" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "organizations:CreateOrganization", "organizations:DescribeOrganization", "iam:CreateServiceLinkedRole", "organizations:ListRoots" ]
    },
    "read" : {
      "permissions" : [ "organizations:DescribeOrganization", "organizations:ListRoots" ]
    },
    "delete" : {
      "permissions" : [ "organizations:DeleteOrganization", "organizations:DescribeOrganization" ]
    },
    "list" : {
      "permissions" : [ "organizations:DescribeOrganization" ]
    },
    "update" : {
      "permissions" : [ "organizations:DescribeOrganization" ]
    }
  },
  "readOnlyProperties" : [ "/properties/Id", "/properties/Arn", "/properties/ManagementAccountArn", "/properties/ManagementAccountId", "/properties/ManagementAccountEmail", "/properties/RootId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "additionalProperties" : False
}