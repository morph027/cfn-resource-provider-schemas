SCHEMA = {
  "typeName" : "AWS::Detective::OrganizationAdmin",
  "description" : "Resource schema for AWS::Detective::OrganizationAdmin",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-detective.git",
  "properties" : {
    "AccountId" : {
      "description" : "The account ID of the account that should be registered as your Organization's delegated administrator for Detective",
      "type" : "string",
      "pattern" : "[0-9]{12}"
    },
    "GraphArn" : {
      "type" : "string",
      "description" : "The Detective graph ARN"
    }
  },
  "additionalProperties" : False,
  "readOnlyProperties" : [ "/properties/GraphArn" ],
  "required" : [ "AccountId" ],
  "primaryIdentifier" : [ "/properties/AccountId" ],
  "createOnlyProperties" : [ "/properties/AccountId" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "detective:EnableOrganizationAdminAccount", "detective:ListOrganizationAdminAccount", "iam:CreateServiceLinkedRole", "organizations:RegisterDelegatedAdministrator", "organizations:DescribeOrganization", "organizations:EnableAWSServiceAccess", "organizations:ListAccounts" ]
    },
    "read" : {
      "permissions" : [ "detective:ListOrganizationAdminAccount", "organizations:DescribeOrganization" ]
    },
    "update" : {
      "permissions" : [ ]
    },
    "delete" : {
      "permissions" : [ "detective:DisableOrganizationAdminAccount", "detective:ListOrganizationAdminAccount", "organizations:DescribeOrganization" ]
    },
    "list" : {
      "permissions" : [ "detective:ListOrganizationAdminAccount", "organizations:DescribeOrganization" ]
    }
  }
}