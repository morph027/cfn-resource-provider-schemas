SCHEMA = {
  "typeName" : "AWS::SecurityHub::DelegatedAdmin",
  "description" : "The ``AWS::SecurityHub::DelegatedAdmin`` resource designates the delegated ASHlong administrator account for an organization. You must enable the integration between ASH and AOlong before you can designate a delegated ASH administrator. Only the management account for an organization can designate the delegated ASH administrator account. For more information, see [Designating the delegated administrator](https://docs.aws.amazon.com/securityhub/latest/userguide/designate-orgs-admin-account.html#designate-admin-instructions) in the *User Guide*.\n To change the delegated administrator account, remove the current delegated administrator account, and then designate the new account.\n To designate multiple delegated administrators in different organizations and AWS-Regions, we recommend using [mappings](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/mappings-section-structure.html).\n Tags aren't supported for this resource.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "properties" : {
    "DelegatedAdminIdentifier" : {
      "description" : "",
      "type" : "string",
      "pattern" : "^[0-9]{12}/[a-zA-Z0-9-]{1,32}$"
    },
    "AdminAccountId" : {
      "description" : "The AWS-account identifier of the account to designate as the Security Hub administrator account.",
      "type" : "string",
      "pattern" : "^[0-9]{12}$"
    },
    "Status" : {
      "description" : "",
      "type" : "string",
      "enum" : [ "ENABLED", "DISABLE_IN_PROGRESS" ]
    }
  },
  "additionalProperties" : False,
  "required" : [ "AdminAccountId" ],
  "createOnlyProperties" : [ "/properties/AdminAccountId" ],
  "readOnlyProperties" : [ "/properties/DelegatedAdminIdentifier", "/properties/Status" ],
  "primaryIdentifier" : [ "/properties/DelegatedAdminIdentifier" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags"
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "securityhub:EnableOrganizationAdminAccount", "organizations:DescribeOrganization", "organizations:EnableAWSServiceAccess", "organizations:RegisterDelegatedAdministrator" ]
    },
    "read" : {
      "permissions" : [ "securityhub:ListOrganizationAdminAccounts", "organizations:DescribeOrganization" ]
    },
    "delete" : {
      "permissions" : [ "securityhub:DisableOrganizationAdminAccount", "organizations:DescribeOrganization" ]
    },
    "list" : {
      "permissions" : [ "securityhub:ListOrganizationAdminAccounts", "organizations:DescribeOrganization" ]
    }
  }
}