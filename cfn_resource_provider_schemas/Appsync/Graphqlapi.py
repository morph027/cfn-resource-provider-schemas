SCHEMA = {
  "typeName" : "AWS::AppSync::GraphQLApi",
  "description" : "Resource Type definition for AWS::AppSync::GraphQLApi",
  "additionalProperties" : False,
  "properties" : {
    "AdditionalAuthenticationProviders" : {
      "type" : "array",
      "description" : "A list of additional authentication providers for the GraphqlApi API.",
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/AdditionalAuthenticationProvider"
      }
    },
    "ApiId" : {
      "description" : "Unique AWS AppSync GraphQL API identifier.",
      "type" : "string"
    },
    "ApiType" : {
      "description" : "The value that indicates whether the GraphQL API is a standard API (GRAPHQL) or merged API (MERGED).",
      "type" : "string"
    },
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) of the API key",
      "type" : "string"
    },
    "AuthenticationType" : {
      "description" : "Security configuration for your GraphQL API",
      "type" : "string"
    },
    "EnhancedMetricsConfig" : {
      "description" : "Enables and controls the enhanced metrics feature. Enhanced metrics emit granular data on API usage and performance such as AppSync request and error counts, latency, and cache hits/misses. All enhanced metric data is sent to your CloudWatch account, and you can configure the types of data that will be sent.",
      "$ref" : "#/definitions/EnhancedMetricsConfig"
    },
    "EnvironmentVariables" : {
      "description" : "A map containing the list of resources with their properties and environment variables.",
      "type" : "object",
      "additionalProperties" : False,
      "patternProperties" : {
        "^[A-Za-z]+\\w*$" : {
          "type" : "string"
        }
      }
    },
    "GraphQLDns" : {
      "description" : "The fully qualified domain name (FQDN) of the endpoint URL of your GraphQL API.",
      "type" : "string"
    },
    "GraphQLEndpointArn" : {
      "description" : "The GraphQL endpoint ARN.",
      "type" : "string"
    },
    "GraphQLUrl" : {
      "description" : "The Endpoint URL of your GraphQL API.",
      "type" : "string"
    },
    "IntrospectionConfig" : {
      "description" : "Sets the value of the GraphQL API to enable (ENABLED) or disable (DISABLED) introspection. If no value is provided, the introspection configuration will be set to ENABLED by default. This field will produce an error if the operation attempts to use the introspection feature while this field is disabled.",
      "type" : "string"
    },
    "LambdaAuthorizerConfig" : {
      "description" : "A LambdaAuthorizerConfig holds configuration on how to authorize AWS AppSync API access when using the AWS_LAMBDA authorizer mode. Be aware that an AWS AppSync API may have only one Lambda authorizer configured at a time.",
      "$ref" : "#/definitions/LambdaAuthorizerConfig"
    },
    "LogConfig" : {
      "description" : "The Amazon CloudWatch Logs configuration.",
      "$ref" : "#/definitions/LogConfig"
    },
    "MergedApiExecutionRoleArn" : {
      "description" : "The AWS Identity and Access Management service role ARN for a merged API. ",
      "type" : "string"
    },
    "Name" : {
      "description" : "The API name",
      "type" : "string"
    },
    "OpenIDConnectConfig" : {
      "description" : "The OpenID Connect configuration.",
      "$ref" : "#/definitions/OpenIDConnectConfig"
    },
    "OwnerContact" : {
      "description" : "The owner contact information for an API resource.",
      "type" : "string"
    },
    "QueryDepthLimit" : {
      "description" : "The maximum depth a query can have in a single request. Depth refers to the amount of nested levels allowed in the body of query.",
      "type" : "integer"
    },
    "RealtimeDns" : {
      "description" : "The fully qualified domain name (FQDN) of the real-time endpoint URL of your GraphQL API.",
      "type" : "string"
    },
    "RealtimeUrl" : {
      "description" : "The GraphQL API real-time endpoint URL.",
      "type" : "string"
    },
    "ResolverCountLimit" : {
      "description" : "The maximum number of resolvers that can be invoked in a single request.",
      "type" : "integer"
    },
    "Tags" : {
      "description" : "An arbitrary set of tags (key-value pairs) for this GraphQL API.\n\n",
      "type" : "array",
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "UserPoolConfig" : {
      "description" : "Optional authorization configuration for using Amazon Cognito user pools with your GraphQL endpoint.\n\n",
      "$ref" : "#/definitions/UserPoolConfig"
    },
    "Visibility" : {
      "description" : "Sets the scope of the GraphQL API to public (GLOBAL) or private (PRIVATE). By default, the scope is set to Global if no value is provided.",
      "type" : "string"
    },
    "XrayEnabled" : {
      "description" : "A flag indicating whether to use AWS X-Ray tracing for this GraphqlApi.\n\n",
      "type" : "boolean"
    }
  },
  "definitions" : {
    "OpenIDConnectConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ClientId" : {
          "description" : "The client identifier of the Relying party at the OpenID identity provider.",
          "type" : "string"
        },
        "AuthTTL" : {
          "description" : "The number of milliseconds that a token is valid after being authenticated.",
          "type" : "number"
        },
        "Issuer" : {
          "description" : "The issuer for the OIDC configuration. ",
          "type" : "string"
        },
        "IatTTL" : {
          "description" : "The number of milliseconds that a token is valid after it's issued to a user.\n\n",
          "type" : "number"
        }
      }
    },
    "EnhancedMetricsConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "OperationLevelMetricsConfig" : {
          "description" : "Controls how operation metrics will be emitted to CloudWatch. Operation metrics include:\n\n",
          "type" : "string"
        },
        "ResolverLevelMetricsBehavior" : {
          "description" : "Controls how resolver metrics will be emitted to CloudWatch. Resolver metrics include:\n\n",
          "type" : "string"
        },
        "DataSourceLevelMetricsBehavior" : {
          "description" : "Controls how data source metrics will be emitted to CloudWatch. Data source metrics include:\n\n",
          "type" : "string"
        }
      },
      "required" : [ "OperationLevelMetricsConfig", "ResolverLevelMetricsBehavior", "DataSourceLevelMetricsBehavior" ]
    },
    "CognitoUserPoolConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AppIdClientRegex" : {
          "description" : "A regular expression for validating the incoming Amazon Cognito user pool app client ID. ",
          "type" : "string"
        },
        "UserPoolId" : {
          "description" : "The user pool ID",
          "type" : "string"
        },
        "AwsRegion" : {
          "description" : "The AWS Region in which the user pool was created.",
          "type" : "string"
        }
      }
    },
    "LambdaAuthorizerConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "IdentityValidationExpression" : {
          "description" : "A regular expression for validation of tokens before the Lambda function is called.",
          "type" : "string"
        },
        "AuthorizerUri" : {
          "description" : "The ARN of the Lambda function to be called for authorization.",
          "type" : "string"
        },
        "AuthorizerResultTtlInSeconds" : {
          "description" : "The number of seconds a response should be cached for.",
          "type" : "integer"
        }
      }
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "type" : "string"
        },
        "Key" : {
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    },
    "UserPoolConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AppIdClientRegex" : {
          "description" : "A regular expression for validating the incoming Amazon Cognito user pool app client ID.",
          "type" : "string"
        },
        "UserPoolId" : {
          "description" : "The user pool ID.",
          "type" : "string"
        },
        "AwsRegion" : {
          "description" : "The AWS Region in which the user pool was created.",
          "type" : "string"
        },
        "DefaultAction" : {
          "description" : "The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pool authentication doesn't match the Amazon Cognito user pool configuration.",
          "type" : "string"
        }
      }
    },
    "AdditionalAuthenticationProvider" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "LambdaAuthorizerConfig" : {
          "$ref" : "#/definitions/LambdaAuthorizerConfig"
        },
        "OpenIDConnectConfig" : {
          "$ref" : "#/definitions/OpenIDConnectConfig"
        },
        "UserPoolConfig" : {
          "$ref" : "#/definitions/CognitoUserPoolConfig"
        },
        "AuthenticationType" : {
          "description" : "The authentication type for API key, AWS Identity and Access Management, OIDC, Amazon Cognito user pools, or AWS Lambda.",
          "type" : "string"
        }
      },
      "required" : [ "AuthenticationType" ]
    },
    "LogConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ExcludeVerboseContent" : {
          "description" : "Set to TRUE to exclude sections that contain information such as headers, context, and evaluated mapping templates, regardless of logging level.",
          "type" : "boolean"
        },
        "FieldLogLevel" : {
          "description" : "The field logging level. Values can be NONE, ERROR, INFO, DEBUG, or ALL.",
          "type" : "string"
        },
        "CloudWatchLogsRoleArn" : {
          "description" : "The service role that AWS AppSync will assume to publish to Amazon CloudWatch Logs in your account.",
          "type" : "string"
        }
      }
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "appsync:TagResource", "appsync:UntagResource", "appsync:ListTagsForResource" ]
  },
  "required" : [ "Name", "AuthenticationType" ],
  "primaryIdentifier" : [ "/properties/ApiId" ],
  "readOnlyProperties" : [ "/properties/ApiId", "/properties/Arn", "/properties/GraphQLEndpointArn", "/properties/GraphQLDns", "/properties/GraphQLUrl", "/properties/RealtimeDns", "/properties/RealtimeUrl" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "appsync:CreateGraphqlApi", "appsync:TagResource" ]
    },
    "read" : {
      "permissions" : [ "appsync:GetGraphqlApi", "appsync:GetGraphqlApiEnvironmentVariables", "appsync:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "appsync:GetGraphqlApi", "appsync:UpdateGraphqlApi", "appsync:TagResource", "appsync:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "appsync:DeleteGraphqlApi" ]
    },
    "list" : {
      "permissions" : [ "appsync:ListGraphqlApis" ]
    }
  }
}