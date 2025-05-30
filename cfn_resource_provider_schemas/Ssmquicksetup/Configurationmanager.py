SCHEMA = {
  "typeName" : "AWS::SSMQuickSetup::ConfigurationManager",
  "description" : "Definition of AWS::SSMQuickSetup::ConfigurationManager Resource Type",
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "tagProperty" : "/properties/Tags",
    "cloudFormationSystemTags" : False,
    "permissions" : [ "ssm-quicksetup:TagResource", "ssm-quicksetup:UntagResource" ]
  },
  "definitions" : {
    "ConfigurationDefinition" : {
      "type" : "object",
      "properties" : {
        "Type" : {
          "type" : "string",
          "pattern" : "^[a-zA-Z0-9_\\-.:/]{3,200}$"
        },
        "Parameters" : {
          "$ref" : "#/definitions/ConfigurationParametersMap"
        },
        "TypeVersion" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1
        },
        "LocalDeploymentExecutionRoleName" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1
        },
        "LocalDeploymentAdministrationRoleArn" : {
          "type" : "string"
        },
        "id" : {
          "type" : "string"
        }
      },
      "required" : [ "Parameters", "Type" ],
      "additionalProperties" : False
    },
    "ConfigurationParametersMap" : {
      "type" : "object",
      "patternProperties" : {
        "^[A-Za-z0-9+=@_\\/\\s-]+$" : {
          "type" : "string",
          "maxLength" : 40960
        }
      },
      "additionalProperties" : False
    },
    "Status" : {
      "type" : "string",
      "enum" : [ "INITIALIZING", "DEPLOYING", "SUCCEEDED", "DELETING", "STOPPING", "FAILED", "STOPPED", "DELETE_FAILED", "STOP_FAILED", "NONE" ]
    },
    "StatusDetails" : {
      "type" : "object",
      "patternProperties" : {
        ".+" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "StatusSummary" : {
      "type" : "object",
      "properties" : {
        "StatusType" : {
          "$ref" : "#/definitions/StatusType"
        },
        "Status" : {
          "$ref" : "#/definitions/Status"
        },
        "StatusMessage" : {
          "type" : "string"
        },
        "LastUpdatedAt" : {
          "type" : "string"
        },
        "StatusDetails" : {
          "$ref" : "#/definitions/StatusDetails"
        }
      },
      "required" : [ "LastUpdatedAt", "StatusType" ],
      "additionalProperties" : False
    },
    "StatusType" : {
      "type" : "string",
      "enum" : [ "Deployment", "AsyncExecutions" ]
    },
    "TagsMap" : {
      "type" : "object",
      "patternProperties" : {
        "^[A-Za-z0-9 +=@_\\/:.-]+$" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1,
          "pattern" : "^[A-Za-z0-9 +=@_\\/:.-]+$"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "ConfigurationDefinitions" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/ConfigurationDefinition"
      }
    },
    "CreatedAt" : {
      "type" : "string"
    },
    "Description" : {
      "type" : "string",
      "pattern" : "^.{0,512}$"
    },
    "LastModifiedAt" : {
      "type" : "string"
    },
    "ManagerArn" : {
      "type" : "string"
    },
    "Name" : {
      "type" : "string",
      "pattern" : "^[ A-Za-z0-9_-]{1,50}$"
    },
    "StatusSummaries" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/StatusSummary"
      }
    },
    "Tags" : {
      "$ref" : "#/definitions/TagsMap"
    }
  },
  "required" : [ "ConfigurationDefinitions" ],
  "readOnlyProperties" : [ "/properties/CreatedAt", "/properties/LastModifiedAt", "/properties/ManagerArn", "/properties/StatusSummaries", "/properties/ConfigurationDefinitions/*/id" ],
  "createOnlyProperties" : [ "/properties/ConfigurationDefinitions/*/Type", "/properties/ConfigurationDefinitions/*/TypeVersion" ],
  "primaryIdentifier" : [ "/properties/ManagerArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:GetRole", "iam:CreateServiceLinkedRole", "iam:ListRoles", "iam:PassRole", "ssm-quicksetup:CreateConfigurationManager", "ssm-quicksetup:GetConfigurationManager", "ssm-quicksetup:TagResource", "ssm-quicksetup:UntagResource", "ssm-quicksetup:UpdateConfigurationManager", "ssm:Describe*", "ssm:Get*", "ssm:List*", "ssm:DeleteAssociation", "ssm:CreateResourceDataSync", "ssm:UpdateResourceDataSync", "ssm:StartAutomationExecution", "ssm:CreateAssociation", "ssm:StartAssociationsOnce", "cloudformation:List*", "cloudformation:Describe*", "cloudformation:CreateStack", "cloudformation:CreateStackInstances", "cloudformation:CreateStackSet", "cloudformation:DeleteStack", "cloudformation:DeleteStackInstances", "cloudformation:DeleteStackSet", "cloudformation:UpdateStack", "cloudformation:UpdateStackSet", "cloudformation:StopStackSetOperation", "cloudformation:GetTemplate", "cloudformation:RollbackStack", "cloudformation:TagResource", "cloudformation:UntagResource", "organizations:Describe*", "organizations:List*", "organizations:RegisterDelegatedAdministrator", "organizations:DeregisterDelegatedAdministrator", "organizations:EnableAWSServiceAccess" ]
    },
    "read" : {
      "permissions" : [ "ssm-quicksetup:GetConfigurationManager", "iam:GetRole", "iam:PassRole", "iam:ListRoles", "ssm:DescribeDocument", "ssm:GetDocument" ]
    },
    "update" : {
      "permissions" : [ "iam:GetRole", "iam:CreateServiceLinkedRole", "iam:ListRoles", "iam:PassRole", "ssm-quicksetup:GetConfigurationManager", "ssm-quicksetup:TagResource", "ssm-quicksetup:UntagResource", "ssm-quicksetup:UpdateConfigurationManager", "ssm-quicksetup:UpdateConfigurationDefinition", "ssm:Describe*", "ssm:Get*", "ssm:List*", "ssm:DeleteAssociation", "ssm:CreateResourceDataSync", "ssm:UpdateResourceDataSync", "ssm:StartAutomationExecution", "ssm:CreateAssociation", "ssm:StartAssociationsOnce", "cloudformation:List*", "cloudformation:Describe*", "cloudformation:CreateStack", "cloudformation:CreateStackInstances", "cloudformation:CreateStackSet", "cloudformation:DeleteStack", "cloudformation:DeleteStackInstances", "cloudformation:DeleteStackSet", "cloudformation:UpdateStack", "cloudformation:UpdateStackSet", "cloudformation:StopStackSetOperation", "cloudformation:GetTemplate", "cloudformation:RollbackStack", "cloudformation:TagResource", "cloudformation:UntagResource", "organizations:Describe*", "organizations:List*", "organizations:RegisterDelegatedAdministrator", "organizations:DeregisterDelegatedAdministrator", "organizations:EnableAWSServiceAccess" ]
    },
    "delete" : {
      "permissions" : [ "ssm-quicksetup:DeleteConfigurationManager", "iam:GetRole", "iam:CreateServiceLinkedRole", "iam:ListRoles", "iam:PassRole", "ssm-quicksetup:GetConfigurationManager", "ssm-quicksetup:ListConfigurationManagers", "ssm-quicksetup:TagResource", "ssm-quicksetup:UntagResource", "ssm-quicksetup:UpdateConfigurationManager", "ssm:Describe*", "ssm:Get*", "ssm:List*", "ssm:DeleteAssociation", "ssm:CreateResourceDataSync", "ssm:UpdateResourceDataSync", "ssm:StartAutomationExecution", "ssm:CreateAssociation", "ssm:StartAssociationsOnce", "cloudformation:List*", "cloudformation:Describe*", "cloudformation:CreateStack", "cloudformation:CreateStackInstances", "cloudformation:CreateStackSet", "cloudformation:DeleteStack", "cloudformation:DeleteStackInstances", "cloudformation:DeleteStackSet", "cloudformation:UpdateStack", "cloudformation:UpdateStackSet", "cloudformation:StopStackSetOperation", "cloudformation:GetTemplate", "cloudformation:RollbackStack", "cloudformation:TagResource", "cloudformation:UntagResource", "organizations:Describe*", "organizations:List*", "organizations:RegisterDelegatedAdministrator", "organizations:DeregisterDelegatedAdministrator", "organizations:EnableAWSServiceAccess" ]
    },
    "list" : {
      "permissions" : [ "ssm-quicksetup:ListConfigurationManagers" ]
    }
  },
  "additionalProperties" : False
}