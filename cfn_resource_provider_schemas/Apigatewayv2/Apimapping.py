SCHEMA = {
  "typeName" : "AWS::ApiGatewayV2::ApiMapping",
  "description" : "The ``AWS::ApiGatewayV2::ApiMapping`` resource contains an API mapping. An API mapping relates a path of your custom domain name to a stage of your API. A custom domain name can have multiple API mappings, but the paths can't overlap. A custom domain can map only to APIs of the same protocol type. For more information, see [CreateApiMapping](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/domainnames-domainname-apimappings.html#CreateApiMapping) in the *Amazon API Gateway V2 API Reference*.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-apigatewayv2.git",
  "properties" : {
    "ApiMappingId" : {
      "description" : "",
      "type" : "string"
    },
    "DomainName" : {
      "description" : "The domain name.",
      "type" : "string"
    },
    "Stage" : {
      "description" : "The API stage.",
      "type" : "string"
    },
    "ApiMappingKey" : {
      "description" : "The API mapping key.",
      "type" : "string"
    },
    "ApiId" : {
      "description" : "The identifier of the API.",
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "required" : [ "DomainName", "Stage", "ApiId" ],
  "createOnlyProperties" : [ "/properties/DomainName" ],
  "primaryIdentifier" : [ "/properties/ApiMappingId", "/properties/DomainName" ],
  "readOnlyProperties" : [ "/properties/ApiMappingId" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "apigateway:POST" ]
    },
    "update" : {
      "permissions" : [ "apigateway:PATCH", "apigateway:GET", "apigateway:PUT" ]
    },
    "read" : {
      "permissions" : [ "apigateway:GET" ]
    },
    "delete" : {
      "permissions" : [ "apigateway:DELETE" ]
    },
    "list" : {
      "permissions" : [ "apigateway:GET" ]
    }
  }
}