<?php
// Receptor temporal de fotogramas (los manda el navegador de Eliam desde YouTube). Solo con el token.
$TOKEN = '3f893fbd56c7e417d5d79dfb';
header('Access-Control-Allow-Origin: https://www.youtube.com');
header('Access-Control-Allow-Headers: Content-Type');
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') exit;
$in = json_decode(file_get_contents('php://input'), true) ?: [];
if (($in['token'] ?? '') !== $TOKEN) { http_response_code(403); exit('no'); }
$dir = __DIR__ . '/out'; if (!is_dir($dir)) mkdir($dir, 0755, true);
$name = preg_replace('/[^a-z0-9_-]/i', '', $in['name'] ?? '');
$data = $in['data'] ?? '';
if (!$name || strpos($data, 'data:image/jpeg;base64,') !== 0) { http_response_code(400); exit('bad'); }
file_put_contents("$dir/$name.jpg", base64_decode(substr($data, 23)));
echo "ok $name " . filesize("$dir/$name.jpg");
