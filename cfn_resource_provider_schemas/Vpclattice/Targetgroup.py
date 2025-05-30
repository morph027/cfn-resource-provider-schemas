SCHEMA = {
  "typeName" : "AWS::VpcLattice::TargetGroup",
  "description" : "A target group is a collection of targets, or compute resources, that run your application or service. A target group can only be used by a single service.",
  "additionalProperties" : False,
  "definitions" : {
    "HealthCheckConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Enabled" : {
          "type" : "boolean"
        },
        "Protocol" : {
          "type" : "string",
          "enum" : [ "HTTP", "HTTPS" ]
        },
        "ProtocolVersion" : {
          "type" : "string",
          "enum" : [ "HTTP1", "HTTP2" ]
        },
        "Port" : {
          "type" : "integer",
          "maximum" : 65535,
          "minimum" : 1
        },
        "Path" : {
          "type" : "string",
          "maxLength" : 2048,
          "minLength" : 0,
          "pattern" : "(^/[a-zA-Z0-9@:%_+.~#?&/=-]*$|(^$))"
        },
        "HealthCheckIntervalSeconds" : {
          "type" : "integer",
          "maximum" : 300,
          "minimum" : 5
        },
        "HealthCheckTimeoutSeconds" : {
          "type" : "integer",
          "maximum" : 120,
          "minimum" : 1
        },
        "HealthyThresholdCount" : {
          "type" : "integer",
          "maximum" : 10,
          "minimum" : 2
        },
        "UnhealthyThresholdCount" : {
          "type" : "integer",
          "maximum" : 10,
          "minimum" : 2
        },
        "Matcher" : {
          "$ref" : "#/definitions/Matcher"
        }
      }
    },
    "Matcher" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "HttpCode" : {
          "type" : "string",
          "minLength" : 3,
          "maxLength" : 2000,
          "pattern" : "^[0-9-,]+$"
        }
      },
      "required" : [ "HttpCode" ]
    },
    "TargetGroupConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Port" : {
          "type" : "integer",
          "maximum" : 65535,
          "minimum" : 1
        },
        "Protocol" : {
          "type" : "string",
          "enum" : [ "HTTP", "HTTPS", "TCP" ]
        },
        "ProtocolVersion" : {
          "type" : "string",
          "default" : "HTTP1",
          "enum" : [ "HTTP1", "HTTP2", "GRPC" ]
        },
        "IpAddressType" : {
          "type" : "string",
          "default" : "IPV4",
          "enum" : [ "IPV4", "IPV6" ]
        },
        "LambdaEventStructureVersion" : {
          "type" : "string",
          "enum" : [ "V1", "V2" ]
        },
        "VpcIdentifier" : {
          "type" : "string",
          "maxLength" : 2048,
          "minLength" : 5,
          "pattern" : "^vpc-(([0-9a-z]{8})|([0-9a-z]{17}))$"
        },
        "HealthCheck" : {
          "$ref" : "#/definitions/HealthCheckConfig"
        }
      },
      "required" : [ ]
    },
    "Target" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Id" : {
          "type" : "string"
        },
        "Port" : {
          "type" : "integer",
          "maximum" : 65535,
          "minimum" : 1
        }
      },
      "required" : [ "Id" ]
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ]
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^arn:[a-z0-9\\-]+:vpc-lattice:[a-zA-Z0-9\\-]+:\\d{12}:targetgroup/tg-[0-9a-z]{17}$"
    },
    "Config" : {
      "$ref" : "#/definitions/TargetGroupConfig"
    },
    "CreatedAt" : {
      "type" : "string"
    },
    "Id" : {
      "type" : "string",
      "maxLength" : 20,
      "minLength" : 20,
      "pattern" : "^tg-[0-9a-z]{17}$"
    },
    "LastUpdatedAt" : {
      "type" : "string"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 128,
      "minLength" : 3,
      "pattern" : "^(?!tg-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+$"
    },
    "Status" : {
      "type" : "string",
      "enum" : [ "CREATE_IN_PROGRESS", "ACTIVE", "DELETE_IN_PROGRESS", "CREATE_FAILED", "DELETE_FAILED" ]
    },
    "Type" : {
      "type" : "string",
      "enum" : [ "IP", "LAMBDA", "INSTANCE", "ALB" ]
    },
    "Targets" : {
      "type" : "array",
      "insertionOrder" : False,
      "minItems" : 0,
      "maxItems" : 100,
      "default" : [ ],
      "items" : {
        "$ref" : "#/definitions/Target"
      }
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : True,
      "minItems" : 0,
      "maxItems" : 50,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "required" : [ "Type" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CreatedAt", "/properties/Id", "/properties/LastUpdatedAt", "/properties/Status" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/Type", "/properties/Config/Port", "/properties/Config/IpAddressType", "/properties/Config/Protocol", "/properties/Config/ProtocolVersion", "/properties/Config/VpcIdentifier", "/properties/Config/LambdaEventStructureVersion" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "additionalIdentifiers" : [ [ "/properties/Id" ], [ "/properties/Name" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "vpc-lattice:CreateTargetGroup", "vpc-lattice:GetTargetGroup", "vpc-lattice:RegisterTargets", "vpc-lattice:ListTargets", "vpc-lattice:ListTagsForResource", "vpc-lattice:TagResource", "vpc-lattice:UntagResource", "ec2:DescribeVpcs", "ec2:DescribeInstances", "ec2:DescribeSubnets", "ec2:DescribeAvailabilityZoneMappings", "lambda:Invoke", "lambda:AddPermission", "elasticloadbalancing:DescribeLoadBalancers", "iam:CreateServiceLinkedRole" ]
    },
    "read" : {
      "permissions" : [ "vpc-lattice:GetTargetGroup", "vpc-lattice:ListTargets", "vpc-lattice:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "vpc-lattice:UpdateTargetGroup", "vpc-lattice:GetTargetGroup", "vpc-lattice:ListTargets", "vpc-lattice:RegisterTargets", "vpc-lattice:DeregisterTargets", "ec2:DescribeVpcs", "ec2:DescribeInstances", "ec2:DescribeSubnets", "ec2:DescribeAvailabilityZoneMappings", "elasticloadbalancing:DescribeLoadBalancers", "lambda:Invoke", "lambda:RemovePermission", "lambda:AddPermission", "vpc-lattice:TagResource", "vpc-lattice:UntagResource", "vpc-lattice:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "vpc-lattice:DeleteTargetGroup", "vpc-lattice:GetTargetGroup", "vpc-lattice:DeregisterTargets", "vpc-lattice:ListTargets", "lambda:RemovePermission" ]
    },
    "list" : {
      "permissions" : [ "vpc-lattice:ListTargetGroups" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "vpc-lattice:UntagResource", "vpc-lattice:TagResource", "vpc-lattice:ListTagsForResource" ]
  }
}