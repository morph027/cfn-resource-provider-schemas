SCHEMA = {
  "typeName" : "AWS::SecurityHub::PolicyAssociation",
  "description" : "The AWS::SecurityHub::PolicyAssociation resource represents the AWS Security Hub Central Configuration Policy associations in your Target. Only the AWS Security Hub delegated administrator can create the resouce from the home region.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-securityhub",
  "properties" : {
    "ConfigurationPolicyId" : {
      "description" : "The universally unique identifier (UUID) of the configuration policy or a value of SELF_MANAGED_SECURITY_HUB for a self-managed configuration",
      "type" : "string",
      "pattern" : "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^SELF_MANAGED_SECURITY_HUB$"
    },
    "AssociationStatus" : {
      "description" : "The current status of the association between the specified target and the configuration",
      "type" : "string",
      "enum" : [ "SUCCESS", "PENDING", "FAILED" ]
    },
    "AssociationType" : {
      "description" : "Indicates whether the association between the specified target and the configuration was directly applied by the Security Hub delegated administrator or inherited from a parent",
      "type" : "string",
      "enum" : [ "APPLIED", "INHERITED" ]
    },
    "AssociationStatusMessage" : {
      "description" : "An explanation for a FAILED value for AssociationStatus",
      "type" : "string"
    },
    "TargetId" : {
      "description" : "The identifier of the target account, organizational unit, or the root",
      "type" : "string"
    },
    "TargetType" : {
      "description" : "Indicates whether the target is an AWS account, organizational unit, or the organization root",
      "type" : "string",
      "enum" : [ "ACCOUNT", "ORGANIZATIONAL_UNIT", "ROOT" ]
    },
    "UpdatedAt" : {
      "description" : "The date and time, in UTC and ISO 8601 format, that the configuration policy association was last updated",
      "type" : "string"
    },
    "AssociationIdentifier" : {
      "description" : "A unique identifier to indicates if the target has an association",
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "required" : [ "TargetId", "TargetType", "ConfigurationPolicyId" ],
  "readOnlyProperties" : [ "/properties/AssociationStatus", "/properties/AssociationType", "/properties/AssociationStatusMessage", "/properties/UpdatedAt", "/properties/AssociationIdentifier" ],
  "createOnlyProperties" : [ "/properties/TargetId", "/properties/TargetType" ],
  "primaryIdentifier" : [ "/properties/AssociationIdentifier" ],
  "tagging" : {
    "taggable" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "securityhub:StartConfigurationPolicyAssociation", "securityhub:GetConfigurationPolicyAssociation" ],
      "timeoutInMinutes" : 1440
    },
    "read" : {
      "permissions" : [ "securityhub:GetConfigurationPolicyAssociation", "securityhub:GetConfigurationPolicyAssociation" ]
    },
    "update" : {
      "permissions" : [ "securityhub:StartConfigurationPolicyAssociation", "securityhub:GetConfigurationPolicyAssociation" ],
      "timeoutInMinutes" : 1440
    },
    "delete" : {
      "permissions" : [ "securityhub:StartConfigurationPolicyDisassociation", "securityhub:GetConfigurationPolicyAssociation" ]
    },
    "list" : {
      "permissions" : [ "securityhub:ListConfigurationPolicyAssociations" ]
    }
  }
}