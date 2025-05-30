SCHEMA = {
  "typeName" : "AWS::Macie::Session",
  "description" : "The AWS::Macie::Session resource specifies a new Amazon Macie session. A session is an object that represents the Amazon Macie service. A session is required for Amazon Macie to become operational.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-macie.git",
  "properties" : {
    "AwsAccountId" : {
      "description" : "AWS account ID of customer",
      "type" : "string"
    },
    "Status" : {
      "description" : "A enumeration value that specifies the status of the Macie Session.",
      "type" : "string",
      "enum" : [ "ENABLED", "PAUSED" ],
      "default" : "ENABLED"
    },
    "FindingPublishingFrequency" : {
      "description" : "A enumeration value that specifies how frequently finding updates are published.",
      "type" : "string",
      "enum" : [ "FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS" ],
      "default" : "SIX_HOURS"
    },
    "ServiceRole" : {
      "description" : "Service role used by Macie",
      "type" : "string"
    },
    "AutomatedDiscoveryStatus" : {
      "description" : "The status of automated sensitive data discovery for the Macie session.",
      "type" : "string",
      "enum" : [ "ENABLED", "DISABLED" ]
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "primaryIdentifier" : [ "/properties/AwsAccountId" ],
  "readOnlyProperties" : [ "/properties/AwsAccountId", "/properties/ServiceRole", "/properties/AutomatedDiscoveryStatus" ],
  "additionalProperties" : False,
  "handlers" : {
    "create" : {
      "permissions" : [ "macie2:GetMacieSession", "macie2:EnableMacie", "macie2:ListAutomatedDiscoveryAccounts" ]
    },
    "read" : {
      "permissions" : [ "macie2:GetMacieSession", "macie2:ListAutomatedDiscoveryAccounts" ]
    },
    "list" : {
      "permissions" : [ "macie2:GetMacieSession", "macie2:ListAutomatedDiscoveryAccounts" ]
    },
    "update" : {
      "permissions" : [ "macie2:GetMacieSession", "macie2:UpdateMacieSession", "macie2:ListAutomatedDiscoveryAccounts" ]
    },
    "delete" : {
      "permissions" : [ "macie2:DisableMacie" ]
    }
  }
}