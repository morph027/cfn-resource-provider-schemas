SCHEMA = {
  "typeName" : "AWS::RefactorSpaces::Route",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-refactor-spaces",
  "description" : "Definition of AWS::RefactorSpaces::Route Resource Type",
  "definitions" : {
    "RouteActivationState" : {
      "type" : "string",
      "enum" : [ "INACTIVE", "ACTIVE" ]
    },
    "Method" : {
      "type" : "string",
      "enum" : [ "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT" ]
    },
    "RouteType" : {
      "type" : "string",
      "enum" : [ "DEFAULT", "URI_PATH" ]
    },
    "DefaultRouteInput" : {
      "type" : "object",
      "properties" : {
        "ActivationState" : {
          "$ref" : "#/definitions/RouteActivationState"
        }
      },
      "required" : [ "ActivationState" ],
      "additionalProperties" : False
    },
    "UriPathRouteInput" : {
      "type" : "object",
      "properties" : {
        "SourcePath" : {
          "type" : "string",
          "maxLength" : 2048,
          "minLength" : 1,
          "pattern" : "^(/([a-zA-Z0-9._:-]+|\\{[a-zA-Z0-9._:-]+\\}))+$"
        },
        "ActivationState" : {
          "$ref" : "#/definitions/RouteActivationState"
        },
        "Methods" : {
          "type" : "array",
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/Method"
          }
        },
        "IncludeChildPaths" : {
          "type" : "boolean"
        },
        "AppendSourcePath" : {
          "type" : "boolean"
        }
      },
      "required" : [ "ActivationState" ],
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
    "PathResourceToId" : {
      "type" : "string"
    },
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
    "EnvironmentIdentifier" : {
      "type" : "string",
      "maxLength" : 14,
      "minLength" : 14,
      "pattern" : "^env-([0-9A-Za-z]{10}$)"
    },
    "RouteIdentifier" : {
      "type" : "string",
      "maxLength" : 14,
      "minLength" : 14,
      "pattern" : "^rte-([0-9A-Za-z]{10}$)"
    },
    "RouteType" : {
      "$ref" : "#/definitions/RouteType"
    },
    "ServiceIdentifier" : {
      "type" : "string",
      "maxLength" : 14,
      "minLength" : 14,
      "pattern" : "^svc-([0-9A-Za-z]{10}$)"
    },
    "DefaultRoute" : {
      "$ref" : "#/definitions/DefaultRouteInput"
    },
    "UriPathRoute" : {
      "$ref" : "#/definitions/UriPathRouteInput"
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
  "required" : [ "EnvironmentIdentifier", "ApplicationIdentifier", "ServiceIdentifier", "RouteType" ],
  "readOnlyProperties" : [ "/properties/RouteIdentifier", "/properties/PathResourceToId", "/properties/Arn" ],
  "writeOnlyProperties" : [ "/properties/RouteType", "/properties/ServiceIdentifier", "/properties/DefaultRoute", "/properties/UriPathRoute" ],
  "createOnlyProperties" : [ "/properties/ApplicationIdentifier", "/properties/EnvironmentIdentifier", "/properties/RouteType", "/properties/ServiceIdentifier", "/properties/UriPathRoute/SourcePath", "/properties/UriPathRoute/Methods", "/properties/UriPathRoute/IncludeChildPaths", "/properties/UriPathRoute/AppendSourcePath" ],
  "primaryIdentifier" : [ "/properties/EnvironmentIdentifier", "/properties/ApplicationIdentifier", "/properties/RouteIdentifier" ],
  "additionalProperties" : False,
  "handlers" : {
    "create" : {
      "permissions" : [ "refactor-spaces:CreateRoute", "refactor-spaces:GetRoute", "refactor-spaces:TagResource", "iam:CreateServiceLinkedRole", "apigateway:GET", "apigateway:PATCH", "apigateway:POST", "apigateway:PUT", "apigateway:DELETE", "apigateway:UpdateRestApiPolicy", "lambda:GetFunctionConfiguration", "lambda:AddPermission", "elasticloadbalancing:DescribeListeners", "elasticloadbalancing:DescribeTargetGroups", "elasticloadbalancing:CreateListener", "elasticloadbalancing:CreateTargetGroup", "elasticloadbalancing:DescribeTags", "elasticloadbalancing:AddTags", "elasticloadbalancing:RegisterTargets", "elasticloadbalancing:DescribeTargetHealth", "ec2:DescribeSubnets", "tag:GetResources" ]
    },
    "read" : {
      "permissions" : [ "refactor-spaces:GetRoute", "refactor-spaces:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "refactor-spaces:DeleteRoute", "refactor-spaces:GetRoute", "refactor-spaces:UntagResource", "apigateway:GET", "apigateway:PATCH", "apigateway:POST", "apigateway:PUT", "apigateway:DELETE", "apigateway:UpdateRestApiPolicy", "lambda:GetFunctionConfiguration", "lambda:AddPermission", "elasticloadbalancing:DescribeListeners", "elasticloadbalancing:DescribeTargetGroups", "elasticloadbalancing:CreateListener", "elasticloadbalancing:CreateTargetGroup", "elasticloadbalancing:DeleteListener", "elasticloadbalancing:DeleteTargetGroup", "elasticloadbalancing:DescribeTags", "elasticloadbalancing:AddTags", "elasticloadbalancing:RegisterTargets", "elasticloadbalancing:DescribeTargetHealth", "ec2:DescribeSubnets", "tag:GetResources" ]
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
      "permissions" : [ "refactor-spaces:ListRoutes", "refactor-spaces:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "refactor-spaces:UpdateRoute", "refactor-spaces:GetRoute", "refactor-spaces:TagResource", "iam:CreateServiceLinkedRole", "apigateway:GET", "apigateway:PATCH", "apigateway:POST", "apigateway:PUT", "apigateway:DELETE", "apigateway:UpdateRestApiPolicy", "lambda:GetFunctionConfiguration", "lambda:AddPermission", "elasticloadbalancing:DescribeListeners", "elasticloadbalancing:DescribeTargetGroups", "elasticloadbalancing:CreateListener", "elasticloadbalancing:CreateTargetGroup", "elasticloadbalancing:DeleteListener", "elasticloadbalancing:DeleteTargetGroup", "elasticloadbalancing:DescribeTags", "elasticloadbalancing:AddTags", "elasticloadbalancing:RegisterTargets", "elasticloadbalancing:DescribeTargetHealth", "ec2:DescribeSubnets", "ec2:DescribeSubnets", "tag:GetResources" ]
    }
  },
  "taggable" : True
}