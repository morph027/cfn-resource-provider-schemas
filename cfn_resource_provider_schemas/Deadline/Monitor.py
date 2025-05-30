SCHEMA = {
  "typeName" : "AWS::Deadline::Monitor",
  "description" : "Definition of AWS::Deadline::Monitor Resource Type",
  "properties" : {
    "DisplayName" : {
      "type" : "string",
      "maxLength" : 100,
      "minLength" : 1
    },
    "IdentityCenterApplicationArn" : {
      "type" : "string"
    },
    "IdentityCenterInstanceArn" : {
      "type" : "string",
      "pattern" : "^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}$"
    },
    "MonitorId" : {
      "type" : "string",
      "pattern" : "^monitor-[0-9a-f]{32}$"
    },
    "RoleArn" : {
      "type" : "string",
      "pattern" : "^arn:(aws[a-zA-Z-]*):iam::\\d{12}:role(/[!-.0-~]+)*/[\\w+=,.@-]+$"
    },
    "Subdomain" : {
      "type" : "string",
      "pattern" : "^[a-z0-9-]{1,100}$"
    },
    "Url" : {
      "type" : "string"
    },
    "Arn" : {
      "type" : "string",
      "pattern" : "^arn:(aws[a-zA-Z-]*):deadline:[a-z0-9-]+:[0-9]+:monitor/monitor-[0-9a-z]{32}$"
    }
  },
  "required" : [ "DisplayName", "IdentityCenterInstanceArn", "RoleArn", "Subdomain" ],
  "readOnlyProperties" : [ "/properties/IdentityCenterApplicationArn", "/properties/MonitorId", "/properties/Url", "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/IdentityCenterInstanceArn" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "deadline:CreateMonitor", "deadline:GetMonitor", "iam:PassRole", "kms:CreateGrant", "sso:CreateApplication", "sso:DeleteApplication", "sso:PutApplicationAssignmentConfiguration", "sso:PutApplicationAuthenticationMethod", "sso:PutApplicationGrant" ]
    },
    "read" : {
      "permissions" : [ "deadline:GetMonitor" ]
    },
    "update" : {
      "permissions" : [ "deadline:GetMonitor", "deadline:UpdateMonitor", "iam:PassRole", "kms:CreateGrant", "sso:PutApplicationGrant", "sso:UpdateApplication" ]
    },
    "delete" : {
      "permissions" : [ "deadline:DeleteMonitor", "deadline:GetMonitor", "sso:DeleteApplication" ]
    },
    "list" : {
      "permissions" : [ "deadline:ListMonitors" ]
    }
  },
  "additionalProperties" : False
}