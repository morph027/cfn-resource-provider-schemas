SCHEMA = {
  "typeName" : "AWS::RDS::DBProxyTargetGroup",
  "description" : "Resource schema for AWS::RDS::DBProxyTargetGroup",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-rds-proxy",
  "definitions" : {
    "ConnectionPoolConfigurationInfoFormat" : {
      "type" : "object",
      "properties" : {
        "MaxConnectionsPercent" : {
          "description" : "The maximum size of the connection pool for each target in a target group.",
          "type" : "integer",
          "minimum" : 0,
          "maximum" : 100
        },
        "MaxIdleConnectionsPercent" : {
          "description" : "Controls how actively the proxy closes idle database connections in the connection pool.",
          "type" : "integer",
          "minimum" : 0,
          "maximum" : 100
        },
        "ConnectionBorrowTimeout" : {
          "description" : "The number of seconds for a proxy to wait for a connection to become available in the connection pool.",
          "type" : "integer"
        },
        "SessionPinningFilters" : {
          "description" : "Each item in the list represents a class of SQL operations that normally cause all later statements in a session using a proxy to be pinned to the same underlying database connection.",
          "type" : "array",
          "insertionOrder" : False,
          "items" : {
            "type" : "string"
          }
        },
        "InitQuery" : {
          "description" : "One or more SQL statements for the proxy to run when opening each new database connection.",
          "type" : "string"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "DBProxyName" : {
      "description" : "The identifier for the proxy.",
      "type" : "string",
      "pattern" : "[A-z][0-z]*",
      "maxLength" : 64
    },
    "TargetGroupArn" : {
      "description" : "The Amazon Resource Name (ARN) representing the target group.",
      "type" : "string"
    },
    "TargetGroupName" : {
      "description" : "The identifier for the DBProxyTargetGroup",
      "type" : "string",
      "enum" : [ "default" ]
    },
    "ConnectionPoolConfigurationInfo" : {
      "$ref" : "#/definitions/ConnectionPoolConfigurationInfoFormat"
    },
    "DBInstanceIdentifiers" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "DBClusterIdentifiers" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    }
  },
  "additionalProperties" : False,
  "required" : [ "DBProxyName", "TargetGroupName" ],
  "readOnlyProperties" : [ "/properties/TargetGroupArn" ],
  "createOnlyProperties" : [ "/properties/DBProxyName", "/properties/TargetGroupName" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "primaryIdentifier" : [ "/properties/TargetGroupArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "rds:DescribeDBProxies", "rds:DescribeDBProxyTargetGroups", "rds:ModifyDBProxyTargetGroup", "rds:RegisterDBProxyTargets" ]
    },
    "read" : {
      "permissions" : [ "rds:DescribeDBProxyTargetGroups", "rds:DescribeDBProxyTargets" ]
    },
    "update" : {
      "permissions" : [ "rds:DescribeDBProxyTargetGroups", "rds:ModifyDBProxyTargetGroup", "rds:RegisterDBProxyTargets", "rds:DeregisterDBProxyTargets" ]
    },
    "delete" : {
      "permissions" : [ "rds:DeregisterDBProxyTargets" ]
    },
    "list" : {
      "permissions" : [ "rds:DescribeDBProxyTargetGroups" ]
    }
  }
}