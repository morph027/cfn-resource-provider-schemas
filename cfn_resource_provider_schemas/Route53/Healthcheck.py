SCHEMA = {
  "typeName" : "AWS::Route53::HealthCheck",
  "description" : "Resource schema for AWS::Route53::HealthCheck.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-route53.git",
  "definitions" : {
    "AlarmIdentifier" : {
      "description" : "A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether the specified health check is healthy.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Name" : {
          "description" : "The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        },
        "Region" : {
          "description" : "For the CloudWatch alarm that you want Route 53 health checkers to use to determine whether this health check is healthy, the region that the alarm was created in.",
          "type" : "string"
        }
      },
      "required" : [ "Name", "Region" ]
    },
    "HealthCheckTag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag.",
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag.",
          "maxLength" : 256
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "properties" : {
    "HealthCheckId" : {
      "type" : "string"
    },
    "HealthCheckConfig" : {
      "description" : "A complex type that contains information about the health check.",
      "type" : "object",
      "properties" : {
        "AlarmIdentifier" : {
          "$ref" : "#/definitions/AlarmIdentifier"
        },
        "ChildHealthChecks" : {
          "type" : "array",
          "items" : {
            "type" : "string"
          },
          "maxItems" : 256,
          "insertionOrder" : False
        },
        "EnableSNI" : {
          "type" : "boolean"
        },
        "FailureThreshold" : {
          "type" : "integer",
          "minimum" : 1,
          "maximum" : 10
        },
        "FullyQualifiedDomainName" : {
          "type" : "string",
          "maxLength" : 255
        },
        "HealthThreshold" : {
          "type" : "integer",
          "minimum" : 0,
          "maximum" : 256
        },
        "InsufficientDataHealthStatus" : {
          "type" : "string",
          "enum" : [ "Healthy", "LastKnownStatus", "Unhealthy" ]
        },
        "Inverted" : {
          "type" : "boolean"
        },
        "IPAddress" : {
          "type" : "string",
          "maxLength" : 45,
          "pattern" : "^((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$"
        },
        "MeasureLatency" : {
          "type" : "boolean"
        },
        "Port" : {
          "type" : "integer",
          "minimum" : 1,
          "maximum" : 65535
        },
        "Regions" : {
          "type" : "array",
          "items" : {
            "type" : "string"
          },
          "maxItems" : 64,
          "insertionOrder" : False
        },
        "RequestInterval" : {
          "type" : "integer",
          "minimum" : 10,
          "maximum" : 30
        },
        "ResourcePath" : {
          "type" : "string",
          "maxLength" : 255
        },
        "SearchString" : {
          "type" : "string",
          "maxLength" : 255
        },
        "RoutingControlArn" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 255
        },
        "Type" : {
          "type" : "string",
          "enum" : [ "CALCULATED", "CLOUDWATCH_METRIC", "HTTP", "HTTP_STR_MATCH", "HTTPS", "HTTPS_STR_MATCH", "TCP", "RECOVERY_CONTROL" ]
        }
      },
      "required" : [ "Type" ],
      "additionalProperties" : False
    },
    "HealthCheckTags" : {
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "description" : "An array of key-value pairs to apply to this resource.",
      "items" : {
        "$ref" : "#/definitions/HealthCheckTag"
      }
    }
  },
  "additionalProperties" : False,
  "required" : [ "HealthCheckConfig" ],
  "createOnlyProperties" : [ "/properties/HealthCheckConfig/Type", "/properties/HealthCheckConfig/MeasureLatency", "/properties/HealthCheckConfig/RequestInterval" ],
  "readOnlyProperties" : [ "/properties/HealthCheckId" ],
  "primaryIdentifier" : [ "/properties/HealthCheckId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "route53:CreateHealthCheck", "route53:ChangeTagsForResource", "cloudwatch:DescribeAlarms", "route53-recovery-control-config:DescribeRoutingControl" ]
    },
    "read" : {
      "permissions" : [ "route53:GetHealthCheck", "route53:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "route53:UpdateHealthCheck", "route53:ChangeTagsForResource", "route53:ListTagsForResource", "cloudwatch:DescribeAlarms" ]
    },
    "delete" : {
      "permissions" : [ "route53:DeleteHealthCheck" ]
    },
    "list" : {
      "permissions" : [ "route53:ListHealthChecks", "route53:ListTagsForResource" ]
    }
  },
  "taggable" : True
}