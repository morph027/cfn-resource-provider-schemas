SCHEMA = {
  "typeName" : "AWS::RDS::DBProxyEndpoint",
  "description" : "Resource schema for AWS::RDS::DBProxyEndpoint.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "TagFormat" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "pattern" : "(\\w|\\d|\\s|\\\\|-|\\.:=+-)*",
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "pattern" : "(\\w|\\d|\\s|\\\\|-|\\.:=+-)*",
          "maxLength" : 128
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "DBProxyEndpointName" : {
      "description" : "The identifier for the DB proxy endpoint. This name must be unique for all DB proxy endpoints owned by your AWS account in the specified AWS Region.",
      "type" : "string",
      "pattern" : "[0-z]*",
      "maxLength" : 64
    },
    "DBProxyEndpointArn" : {
      "description" : "The Amazon Resource Name (ARN) for the DB proxy endpoint.",
      "type" : "string",
      "pattern" : "arn:aws[A-Za-z0-9-]{0,64}:rds:[A-Za-z0-9-]{1,64}:[0-9]{12}:.*"
    },
    "DBProxyName" : {
      "description" : "The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region.",
      "type" : "string",
      "pattern" : "[0-z]*",
      "maxLength" : 64
    },
    "VpcId" : {
      "description" : "VPC ID to associate with the new DB proxy endpoint.",
      "type" : "string"
    },
    "VpcSecurityGroupIds" : {
      "description" : "VPC security group IDs to associate with the new DB proxy endpoint.",
      "type" : "array",
      "insertionOrder" : False,
      "minItems" : 1,
      "items" : {
        "type" : "string"
      }
    },
    "VpcSubnetIds" : {
      "description" : "VPC subnet IDs to associate with the new DB proxy endpoint.",
      "type" : "array",
      "minItems" : 2,
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "Endpoint" : {
      "description" : "The endpoint that you can use to connect to the DB proxy. You include the endpoint value in the connection string for a database client application.",
      "type" : "string",
      "maxLength" : 256
    },
    "TargetRole" : {
      "description" : "A value that indicates whether the DB proxy endpoint can be used for read/write or read-only operations.",
      "type" : "string",
      "enum" : [ "READ_WRITE", "READ_ONLY" ]
    },
    "IsDefault" : {
      "description" : "A value that indicates whether this endpoint is the default endpoint for the associated DB proxy. Default DB proxy endpoints always have read/write capability. Other endpoints that you associate with the DB proxy can be either read/write or read-only.",
      "type" : "boolean"
    },
    "Tags" : {
      "description" : "An optional set of key-value pairs to associate arbitrary data of your choosing with the DB proxy endpoint.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/TagFormat"
      }
    }
  },
  "additionalProperties" : False,
  "required" : [ "DBProxyName", "DBProxyEndpointName", "VpcSubnetIds" ],
  "readOnlyProperties" : [ "/properties/DBProxyEndpointArn", "/properties/Endpoint", "/properties/VpcId", "/properties/IsDefault" ],
  "createOnlyProperties" : [ "/properties/DBProxyName", "/properties/DBProxyEndpointName", "/properties/VpcSubnetIds" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "rds:AddTagsToResource", "rds:RemoveTagsFromResource", "rds:ListTagsForResource" ]
  },
  "primaryIdentifier" : [ "/properties/DBProxyEndpointName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "rds:CreateDBProxyEndpoint", "rds:DescribeDBProxyEndpoints" ]
    },
    "read" : {
      "permissions" : [ "rds:DescribeDBProxyEndpoints", "rds:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "rds:ModifyDBProxyEndpoint", "rds:AddTagsToResource", "rds:RemoveTagsFromResource" ]
    },
    "delete" : {
      "permissions" : [ "rds:DescribeDBProxyEndpoints", "rds:DeleteDBProxyEndpoint" ]
    },
    "list" : {
      "permissions" : [ "rds:DescribeDBProxyEndpoints" ]
    }
  }
}