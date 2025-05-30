SCHEMA = {
  "typeName" : "AWS::OpsWorksCM::Server",
  "description" : "Resource Type definition for AWS::OpsWorksCM::Server",
  "additionalProperties" : False,
  "properties" : {
    "KeyPair" : {
      "type" : "string",
      "pattern" : ".*",
      "maxLength" : 10000
    },
    "EngineVersion" : {
      "type" : "string",
      "maxLength" : 10000
    },
    "ServiceRoleArn" : {
      "type" : "string",
      "pattern" : "arn:aws:iam::[0-9]{12}:role/.*",
      "maxLength" : 10000
    },
    "DisableAutomatedBackup" : {
      "type" : "boolean"
    },
    "BackupId" : {
      "type" : "string",
      "pattern" : "[a-zA-Z][a-zA-Z0-9\\-\\.\\:]*",
      "maxLength" : 79
    },
    "EngineModel" : {
      "type" : "string",
      "maxLength" : 10000
    },
    "PreferredMaintenanceWindow" : {
      "type" : "string",
      "pattern" : "^((Mon|Tue|Wed|Thu|Fri|Sat|Sun):)?([0-1][0-9]|2[0-3]):[0-5][0-9]$",
      "maxLength" : 10000
    },
    "AssociatePublicIpAddress" : {
      "type" : "boolean"
    },
    "InstanceProfileArn" : {
      "type" : "string",
      "pattern" : "arn:aws:iam::[0-9]{12}:instance-profile/.*",
      "maxLength" : 10000
    },
    "CustomCertificate" : {
      "type" : "string",
      "pattern" : "(?s)\\s*-----BEGIN CERTIFICATE-----.+-----END CERTIFICATE-----\\s*",
      "maxLength" : 2097152
    },
    "PreferredBackupWindow" : {
      "type" : "string",
      "pattern" : "^((Mon|Tue|Wed|Thu|Fri|Sat|Sun):)?([0-1][0-9]|2[0-3]):[0-5][0-9]$",
      "maxLength" : 10000
    },
    "SecurityGroupIds" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "type" : "string",
        "maxLength" : 10000
      }
    },
    "SubnetIds" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "type" : "string",
        "maxLength" : 10000
      }
    },
    "CustomDomain" : {
      "type" : "string",
      "pattern" : "^(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])$",
      "maxLength" : 253
    },
    "Endpoint" : {
      "type" : "string",
      "maxLength" : 10000
    },
    "CustomPrivateKey" : {
      "type" : "string",
      "pattern" : "(?ms)\\s*^-----BEGIN (?-s:.*)PRIVATE KEY-----$.*?^-----END (?-s:.*)PRIVATE KEY-----$\\s*",
      "maxLength" : 4096
    },
    "ServerName" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 40,
      "pattern" : "[a-zA-Z][a-zA-Z0-9\\-]*"
    },
    "EngineAttributes" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/EngineAttribute"
      }
    },
    "BackupRetentionCount" : {
      "type" : "integer",
      "minLength" : 1
    },
    "Arn" : {
      "type" : "string",
      "maxLength" : 10000
    },
    "InstanceType" : {
      "type" : "string",
      "maxLength" : 10000
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Engine" : {
      "type" : "string",
      "maxLength" : 10000
    }
  },
  "definitions" : {
    "EngineAttribute" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "type" : "string",
          "pattern" : "(?s).*",
          "maxLength" : 10000
        },
        "Name" : {
          "type" : "string",
          "pattern" : "(?s).*",
          "maxLength" : 10000
        }
      }
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "type" : "string",
          "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$",
          "minLength" : 0,
          "maxLength" : 256
        },
        "Key" : {
          "type" : "string",
          "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$",
          "minLength" : 1,
          "maxLength" : 128
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "required" : [ "ServiceRoleArn", "InstanceProfileArn", "InstanceType" ],
  "createOnlyProperties" : [ "/properties/KeyPair", "/properties/CustomPrivateKey", "/properties/ServiceRoleArn", "/properties/InstanceType", "/properties/CustomCertificate", "/properties/CustomDomain", "/properties/InstanceProfileArn", "/properties/SecurityGroupIds", "/properties/ServerName", "/properties/SubnetIds", "/properties/BackupId", "/properties/EngineModel", "/properties/AssociatePublicIpAddress", "/properties/EngineVersion", "/properties/Engine" ],
  "primaryIdentifier" : [ "/properties/ServerName" ],
  "readOnlyProperties" : [ "/properties/ServerName", "/properties/Endpoint", "/properties/Arn" ],
  "writeOnlyProperties" : [ "/properties/BackupId", "/properties/CustomCertificate", "/properties/CustomDomain", "/properties/CustomPrivateKey", "/properties/EngineAttributes", "/properties/EngineVersion", "/properties/KeyPair", "/properties/Tags" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "opsworks-cm:CreateServer", "opsworks-cm:DescribeServers", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "opsworks-cm:DeleteServer", "opsworks-cm:DescribeServers" ]
    },
    "update" : {
      "permissions" : [ "opsworks-cm:UpdateServer", "opsworks-cm:TagResource", "opsworks-cm:UntagResource", "opsworks-cm:DescribeServers" ]
    },
    "list" : {
      "permissions" : [ "opsworks-cm:DescribeServers", "opsworks-cm:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "opsworks-cm:DescribeServers" ]
    }
  }
}