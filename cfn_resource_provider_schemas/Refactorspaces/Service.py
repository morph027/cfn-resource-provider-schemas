SCHEMA = {
  "typeName" : "AWS::RefactorSpaces::Service",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-refactor-spaces",
  "description" : "Definition of AWS::RefactorSpaces::Service Resource Type",
  "definitions" : {
    "LambdaEndpointInput" : {
      "type" : "object",
      "properties" : {
        "Arn" : {
          "type" : "string",
          "maxLength" : 2048,
          "minLength" : 1,
          "pattern" : "^arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\\d{1}:\\d{12}:function:[a-zA-Z0-9-_]+(:(\\$LATEST|[a-zA-Z0-9-_]+))?$"
        }
      },
      "required" : [ "Arn" ],
      "additionalProperties" : False
    },
    "ServiceEndpointType" : {
      "type" : "string",
      "enum" : [ "LAMBDA", "URL" ]
    },
    "UrlEndpointInput" : {
      "type" : "object",
      "properties" : {
        "HealthUrl" : {
          "type" : "string",
          "maxLength" : 2048,
          "minLength" : 1,
          "pattern" : "^https?://[-a-zA-Z0-9+\\x38@#/%?=~_|!:,.;]*[-a-zA-Z0-9+\\x38@#/%=~_|]$"
        },
        "Url" : {
          "type" : "string",
          "maxLength" : 2048,
          "minLength" : 1,
          "pattern" : "^https?://[-a-zA-Z0-9+\\x38@#/%?=~_|!:,.;]*[-a-zA-Z0-9+\\x38@#/%=~_|]$"
        }
      },
      "required" : [ "Url" ],
      "additionalProperties" : False
    },
    "Tag" : {
      "description" : "A label for tagging Environment resource",
      "type" : "object",
      "properties" : {
        "Key" : {
          "description" : "A string used to identify this tag",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128,
          "pattern" : "^(?!aws:).+"
        },
        "Value" : {
          "description" : "A string containing the value for the tag",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "minLength" : 20,
      "maxLength" : 2048,
      "pattern" : "^arn:(aws[a-zA-Z-]*)?:refactor-spaces:[a-zA-Z0-9\\-]+:\\w{12}:[a-zA-Z_0-9+=,.@\\-_/]+$"
    },
    "ApplicationIdentifier" : {
      "type" : "string",
      "maxLength" : 14,
      "minLength" : 14,
      "pattern" : "^app-([0-9A-Za-z]{10}$)"
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 256,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9-_\\s\\.\\!\\*\\#\\@\\']+$"
    },
    "EndpointType" : {
      "$ref" : "#/definitions/ServiceEndpointType"
    },
    "EnvironmentIdentifier" : {
      "type" : "string",
      "maxLength" : 14,
      "minLength" : 14,
      "pattern" : "^env-([0-9A-Za-z]{10}$)"
    },
    "LambdaEndpoint" : {
      "$ref" : "#/definitions/LambdaEndpointInput"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 63,
      "minLength" : 3,
      "pattern" : "^(?!svc-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+$"
    },
    "ServiceIdentifier" : {
      "type" : "string",
      "maxLength" : 14,
      "minLength" : 14,
      "pattern" : "^svc-([0-9A-Za-z]{10}$)"
    },
    "UrlEndpoint" : {
      "$ref" : "#/definitions/UrlEndpointInput"
    },
    "VpcId" : {
      "type" : "string",
      "maxLength" : 21,
      "minLength" : 12,
      "pattern" : "^vpc-[-a-f0-9]{8}([-a-f0-9]{9})?$"
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "description" : "Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair."
    }
  },
  "required" : [ "EnvironmentIdentifier", "ApplicationIdentifier", "EndpointType", "Name" ],
  "readOnlyProperties" : [ "/properties/ServiceIdentifier", "/properties/Arn" ],
  "writeOnlyProperties" : [ "/properties/Description", "/properties/EndpointType", "/properties/LambdaEndpoint", "/properties/Name", "/properties/UrlEndpoint", "/properties/VpcId" ],
  "createOnlyProperties" : [ "/properties/Description", "/properties/EndpointType", "/properties/EnvironmentIdentifier", "/properties/ApplicationIdentifier", "/properties/LambdaEndpoint", "/properties/Name", "/properties/UrlEndpoint", "/properties/VpcId" ],
  "primaryIdentifier" : [ "/properties/EnvironmentIdentifier", "/properties/ApplicationIdentifier", "/properties/ServiceIdentifier" ],
  "additionalProperties" : False,
  "handlers" : {
    "create" : {
      "permissions" : [ "refactor-spaces:CreateService", "refactor-spaces:GetService", "refactor-spaces:TagResource", "ec2:DescribeVpcs", "ec2:DescribeSubnets", "ec2:DescribeRouteTables", "ec2:CreateTags", "ec2:CreateTransitGatewayVpcAttachment", "ec2:DescribeTransitGatewayVpcAttachments", "ec2:CreateSecurityGroup", "ec2:AuthorizeSecurityGroupIngress", "ec2:CreateRoute", "lambda:GetFunctionConfiguration" ]
    },
    "read" : {
      "permissions" : [ "refactor-spaces:GetService", "refactor-spaces:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "refactor-spaces:DeleteService", "refactor-spaces:GetService", "refactor-spaces:UntagResource", "ram:DisassociateResourceShare", "ec2:DescribeNetworkInterfaces", "ec2:DescribeRouteTables", "ec2:DescribeTransitGatewayVpcAttachments", "ec2:DescribeSecurityGroups", "ec2:DeleteSecurityGroup", "ec2:DeleteRoute", "ec2:RevokeSecurityGroupIngress", "ec2:DeleteTransitGatewayVpcAttachment", "ec2:DeleteTags" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "EnvironmentIdentifier" : {
            "$ref" : "resource-schema.json#/properties/EnvironmentIdentifier"
          },
          "ApplicationIdentifier" : {
            "$ref" : "resource-schema.json#/properties/ApplicationIdentifier"
          }
        },
        "required" : [ "EnvironmentIdentifier", "ApplicationIdentifier" ]
      },
      "permissions" : [ "refactor-spaces:ListServices", "refactor-spaces:ListTagsForResource" ]
    }
  },
  "taggable" : True
}