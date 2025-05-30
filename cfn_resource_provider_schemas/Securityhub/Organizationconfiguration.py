SCHEMA = {
  "typeName" : "AWS::SecurityHub::OrganizationConfiguration",
  "description" : "The AWS::SecurityHub::OrganizationConfiguration resource represents the configuration of your organization in Security Hub. Only the Security Hub administrator account can create Organization Configuration resource in each region and can opt-in to Central Configuration only in the aggregation region of FindingAggregator.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-securityhub",
  "properties" : {
    "AutoEnable" : {
      "description" : "Whether to automatically enable Security Hub in new member accounts when they join the organization.",
      "type" : "boolean"
    },
    "AutoEnableStandards" : {
      "description" : "Whether to automatically enable Security Hub default standards in new member accounts when they join the organization.",
      "type" : "string",
      "enum" : [ "DEFAULT", "NONE" ]
    },
    "ConfigurationType" : {
      "description" : "Indicates whether the organization uses local or central configuration.",
      "type" : "string",
      "enum" : [ "CENTRAL", "LOCAL" ]
    },
    "Status" : {
      "description" : "Describes whether central configuration could be enabled as the ConfigurationType for the organization.",
      "type" : "string",
      "enum" : [ "PENDING", "ENABLED", "FAILED" ]
    },
    "StatusMessage" : {
      "description" : "Provides an explanation if the value of Status is equal to FAILED when ConfigurationType is equal to CENTRAL.",
      "type" : "string"
    },
    "MemberAccountLimitReached" : {
      "description" : "Whether the maximum number of allowed member accounts are already associated with the Security Hub administrator account.",
      "type" : "boolean"
    },
    "OrganizationConfigurationIdentifier" : {
      "description" : "The identifier of the OrganizationConfiguration being created and assigned as the unique identifier.",
      "type" : "string",
      "pattern" : "^[0-9]{12}/[a-zA-Z0-9-]{1,32}/securityhub-organization-configuration$"
    }
  },
  "additionalProperties" : False,
  "required" : [ "AutoEnable" ],
  "readOnlyProperties" : [ "/properties/OrganizationConfigurationIdentifier", "/properties/Status", "/properties/StatusMessage", "/properties/MemberAccountLimitReached" ],
  "primaryIdentifier" : [ "/properties/OrganizationConfigurationIdentifier" ],
  "tagging" : {
    "taggable" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "securityhub:UpdateOrganizationConfiguration", "securityhub:DescribeOrganizationConfiguration", "organizations:DescribeOrganization" ]
    },
    "read" : {
      "permissions" : [ "securityhub:DescribeOrganizationConfiguration" ]
    },
    "update" : {
      "permissions" : [ "securityhub:UpdateOrganizationConfiguration", "securityhub:DescribeOrganizationConfiguration", "organizations:DescribeOrganization" ]
    },
    "delete" : {
      "permissions" : [ "securityhub:UpdateOrganizationConfiguration", "securityhub:DescribeOrganizationConfiguration", "securityhub:ListFindingAggregators", "organizations:DescribeOrganization" ]
    },
    "list" : {
      "permissions" : [ "securityhub:DescribeOrganizationConfiguration" ]
    }
  }
}